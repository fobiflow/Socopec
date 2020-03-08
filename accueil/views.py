from datetime import date, datetime

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from agence.models import Agence
from agent.models import Agent
from vehicule.models import Vehicule
from historique.models import Historique, Statut, Probleme
import time


@login_required
def accueil(request):
    identifiant = request.user.username
    agent = Agent.objects.get(identifiant=identifiant)
    actu = time.strftime('%A %d-%m-%Y')
    this_year = date.today().year
    int_month = date.today().month
    mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre",
            "Décembre"]
    this_month = mois[int_month - 1]
    nombre_agences = Agence.objects.all().count()
    if request.user.groups.filter(name="administrateur").exists():
        #  Pour le carré actuellement 1 :
        problemes_orange = Probleme.objects.filter(statut="en cours").count()
        problemes_rouge = Probleme.objects.filter(date_signalement=date.today().strftime('%Y-%m-%d 00:00:00.00000')).count()
        #  Pour le carré actuellement 2 :
        vehicules_vendus = Historique.objects.filter(id_statut=Statut.objects.get(statut="Vendu"),
                                                     date_debut__year=date.today().year).count()
        vehicules_vendus_mois = Historique.objects.filter(id_statut=Statut.objects.get(statut="Vendu"),
                                                          date_debut__month=date.today().month).count()
        total_vehicules = Vehicule.objects.all().count()
        # Pour le carré actuellement 3 :
        statuts = []
        res = Statut.objects.all()
        boots = ["", "bg-success", "bg-warning", "bg-danger", "bg-info", "", "bg-success", "bg-warning", "bg-danger", ""]
        i = 0
        for item in res:
            value = Historique.objects.filter(id_statut=item.id, statut="en cours").count()
            pourcentage = int((value * 100) / total_vehicules)
            new = False
            if item.id > 5:
                new = True
            statuts.append({
                'id': item.id, 'statut': item.statut, 'value': value, "boots": boots[i], "pourcentage": pourcentage, 'new': new
            })
            i += 1
        # Pour le carré parité :
        total_agents = Agent.objects.all().count()
        femmes = Agent.objects.filter(sexe="F").count()
        hommes = Agent.objects.filter(sexe="H").count()
        pourcent_femmes = int((total_agents - hommes) * 100 / total_agents)
        pourcent_hommes = int((total_agents - femmes) * 100 / total_agents)
        return render(request, '../templates/accueil/accueilAdmin.html',
                      {'agent': agent,
                       'actu': actu,
                       'this_year': this_year,
                       'this_month': this_month,
                       'total_vehicules': total_vehicules,
                       'vehicules_vendus': vehicules_vendus,
                       'vehicules_vendus_mois': vehicules_vendus_mois,
                       'problemes_orange': problemes_orange,
                       'problemes_rouge': problemes_rouge,
                       'nombre_agences': nombre_agences,
                       'statuts': statuts,
                       'total_agents': total_agents,
                       'femmes': femmes,
                       'hommes': hommes,
                       'pourcent_femmes': pourcent_femmes,
                       'pourcent_hommes': pourcent_hommes})
    else:
        #  Pour le carré actuellement 1 :
        problemes_orange = Probleme.objects.filter(statut="en cours", id_agence=agent.id_agence).count()
        problemes_rouge = Probleme.objects.filter(date_signalement__day=date.today().day, id_agence=agent.id_agence).count()
        #  Pour le carré actuellement 2 :
        vehicules_vendus = Historique.objects.filter(id_agence=agent.id_agence,
                                                     id_statut=Statut.objects.get(statut="Vendu"),
                                                     date_debut__year=date.today().year).count()
        vehicules_vendus_mois = Historique.objects.filter(id_agence=agent.id_agence,
                                                          id_statut=Statut.objects.get(statut="Vendu"),
                                                          date_debut__month=date.today().month).count()
        #  Pour le carré actuellement 2 :
        total_vehicules = Vehicule.objects.filter(id_agence=agent.id_agence).count()
        # Pour le carré actuellement 3 :
        statuts = []
        res = Statut.objects.all()
        boots = ["", "bg-success", "bg-warning", "bg-danger", "bg-info", "", "bg-success", "bg-warning", "bg-danger", ""]
        i = 0
        for item in res:
            value = Historique.objects.filter(id_agence=agent.id_agence, id_statut=item.id).count()
            pourcentage = int((value * 100) / total_vehicules)
            statuts.append({
                'statut': item.statut, 'value': value, "boots": boots[i], "pourcentage": pourcentage
            })
            i += 1
        # Pour le carré parité :
        total_agents = Agent.objects.filter(id_agence=agent.id_agence).count()
        femmes = Agent.objects.filter(id_agence=agent.id_agence, sexe="F").count()
        hommes = Agent.objects.filter(id_agence=agent.id_agence, sexe="H").count()
        pourcent_femmes = int((total_agents - hommes) * 100 / total_agents)
        pourcent_hommes = int((total_agents - femmes) * 100 / total_agents)
        return render(request, '../templates/accueil/accueilUser.html',
                      {'agent': agent,
                       'actu': actu,
                       'this_year': this_year,
                       'this_month': this_month,
                       'total_vehicules': total_vehicules,
                       'vehicules_vendus': vehicules_vendus,
                       'vehicules_vendus_mois': vehicules_vendus_mois,
                       'problemes_orange': problemes_orange,
                       'problemes_rouge': problemes_rouge,
                       'nombre_agences': nombre_agences,
                       'statuts': statuts,
                       'total_agents': total_agents,
                       'femmes': femmes,
                       'hommes': hommes,
                       'pourcent_femmes': pourcent_femmes,
                       'pourcent_hommes': pourcent_hommes})


def connect(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('accueil')
    else:
        error = False

        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('accueil')
            else:
                error = True

        return render(request, 'accueil/login.html', locals())


def disconnect(request):
    logout(request)
    return HttpResponseRedirect('/')


def password(request):
    if request.method == "POST":
        mail = request.POST.get("email")
        return HttpResponseRedirect('/')

    return render(request, 'accueil/password.html', locals())
