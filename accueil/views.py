from datetime import date

from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required

from agence.models import Agence
from agent.models import Agent
from vehicule.models import Vehicule


@login_required
def accueil(request):
    # TODO : ajout des éléments User
    identifiant = request.user.username
    agent = Agent.objects.get(identifiant=identifiant)
    this_year = date.today().year
    int_month = date.today().month
    mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre",
            "Décembre"]
    this_month = mois[int_month - 1]
    nombre_agences = Agence.objects.all().count()
    if request.user.groups.filter(name="administrateur").exists():
        #  Pour le carré actuellement 2 :
        # TODO : véhicules vendus depuis le début + véhicules vendus le mois dernier
        # vehicules_vendus =
        # vehicules_vendus_mois_dernier =
        total_vehicules = Vehicule.objects.all().count()
        # Pour le carré parité :
        total = Agent.objects.all().count()
        femmes = Agent.objects.filter(sexe="F").count()
        hommes = Agent.objects.filter(sexe="H").count()
        return render(request, '../templates/accueil/accueilAdmin.html',
                      {'agent': agent,
                       'this_year': this_year,
                       'this_month': this_month,
                       'total_vehicules': total_vehicules,
                       'nombre_agences': nombre_agences,
                       'total': total,
                       'femmes': femmes,
                       'hommes': hommes})
    else:
        #  Pour le carré actuellement 2 :
        # TODO : véhicules vendus depuis le début + véhicules vendus le mois dernier
        # vehicules_vendus =
        # vehicules_vendus_mois_dernier =
        # Total vehicules pour l'agence !
        total_vehicules = Vehicule.objects.filter(id_agence=agent.id_agence).count()
        # Pour le carré parité :
        total = Agent.objects.filter(id_agence=agent.id_agence).count()
        femmes = Agent.objects.filter(id_agence=agent.id_agence, sexe="F").count()
        hommes = Agent.objects.filter(id_agence=agent.id_agence, sexe="H").count()
        return render(request, '../templates/accueil/accueilUser.html',
                      {'agent': agent,
                       'this_year': this_year,
                       'this_month': this_month,
                       'total_vehicules': total_vehicules,
                       'nombre_agences': nombre_agences,
                       'total': total,
                       'femmes': femmes,
                       'hommes': hommes})


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
