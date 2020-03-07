from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Agence
from agent.models import Agent
from vehicule.models import Vehicule
from historique.models import Historique, Probleme, Statut
from datetime import date


@login_required()
def generate(request):
    identifiant = request.user.username
    agent = Agent.objects.get(identifiant=identifiant)
    # Pour le tableau :
    data = Agence.objects.all()
    agences_table = []
    for item in data:
        administrateur = ""
        email = ""
        if Agent.objects.filter(poste_socopec="administrateur", id_agence=item.id).exists():
            ret = Agent.objects.get(poste_socopec="administrateur", id_agence=item.id)
            administrateur = ret.prenom + " " + ret.nom
            email = ret.email
        if Agent.objects.filter(poste_socopec="Administrateur", id_agence=item.id).exists():
            ret = Agent.objects.get(poste_socopec="Administrateur", id_agence=item.id)
            administrateur = ret.prenom + " " + ret.nom
            email = ret.email
        vehicules_vendus = Historique.objects.filter(id_agence=item.id, id_statut=Statut.objects.get(statut="Vendu")).count()
        agences_table.append({
            'Ville': item.ville,
            'Agence': item.nom,
            'Nb de personne': Agent.objects.filter(id_agence=item.id).count(),
            'Nb de vehicules': Vehicule.objects.filter(id_agence=item.id).count() - vehicules_vendus,
            'Probleme en cours': Probleme.objects.filter(id_agence=item.id, statut="resolu").count(),
            'Vehicules vendus': vehicules_vendus,
            'Responsable de l\'agence': administrateur,
            'Telephone': item.telephone,
            'Mail': email,
            'Vue': '<a href="' + str(item.id) + '"><img alt="acces fiche agence" class="icon" src="../../../static/images/oeuil.svg"/></a>'
        })
    # Vue pour admin :
    if request.user.groups.filter(name="administrateur").exists():
        this_year = date.today().year
        int_month = date.today().month
        #  Pour le carré actuellement
        vehicules_vendus = Historique.objects.filter(id_statut=Statut.objects.get(statut="Vendu"),
                                                     date_debut__year=date.today().year).count()
        vehicules_vendus_mois = Historique.objects.filter(id_statut=Statut.objects.get(statut="Vendu"),
                                                          date_debut=date.today().strftime("%Y-" + str(int_month) + "-%d 00:00:00.0000")).count()
        total_vehicules = Vehicule.objects.all().count()
        mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
        this_month = mois[int_month - 1]
        nombre_agences = Agence.objects.all().count()
        # Pour le formulaire
        if request.method == 'POST':
            if request.POST.get('nom') and \
                    request.POST.get('adresse') and \
                    request.POST.get('code_postal') and \
                    request.POST.get('ville') and \
                    request.POST.get('telephone') and \
                    request.POST.get('photo'):
                new_agence = Agence(
                    nom=request.POST.get('nom'),
                    adresse=request.POST.get('adresse'),
                    complement_adresse=request.POST.get('complement_adresse'),
                    code_postal=request.POST.get('code_postal'),
                    ville=request.POST.get('ville'),
                    telephone=request.POST.get('telephone'),
                    fax=request.POST.get('fax'),
                    photo=request.POST.get('photo')
                )
                new_agence.save()
                return render(request,
                              '../templates/agence/agenceAdmin.html',
                              {'error': False,
                               'confirmation': True,
                               'confirmation_name': request.POST.get('nom'),
                               'agent': agent,
                               'nombre_agences': nombre_agences,
                               'vehicules_vendus': vehicules_vendus,
                               'vehicules_vendus_mois': vehicules_vendus_mois,
                               'data': data,
                               'agences_table': agences_table,
                               'this_year': this_year,
                               'this_month': this_month,
                               'total_vehicules': total_vehicules})
            else:
                return render(request,
                              '../templates/agence/agenceAdmin.html',
                              {'error': True,
                               'agent': agent,
                               'nombre_agences': nombre_agences,
                               'vehicules_vendus': vehicules_vendus,
                               'vehicules_vendus_mois': vehicules_vendus_mois,
                               'data': data,
                               'agences_table': agences_table,
                               'this_year': this_year,
                               'this_month': this_month,
                               'total_vehicules': total_vehicules})
        else:
            return render(request,
                          '../templates/agence/agenceAdmin.html',
                          {'error': False,
                           'confirmation': False,
                           'agent': agent,
                           'nombre_agences': nombre_agences,
                           'vehicules_vendus': vehicules_vendus,
                           'vehicules_vendus_mois': vehicules_vendus_mois,
                           'data': data,
                           'agences_table': agences_table,
                           'this_year': this_year,
                           'this_month': this_month,
                            'total_vehicules': total_vehicules})
    else:
        # USER :
        return render(request, '../templates/agence/agenceUser.html', {'agent': agent, 'agences_table': agences_table})


@login_required()
def fiche(request, id_agence):
    agence = Agence.objects.get(id=id_agence)
    agents = []
    if Agent.objects.filter(id_agence=agence).exists():
        data = Agent.objects.filter(id_agence=agence)
        for agent in data:
            agents.append({
                'Fonction': agent.poste_socopec,
                'Nom': agent.nom,
                'Prénom': agent.prenom,
                'E-mail Pro': agent.email
            })
    problemes = []
    if Probleme.objects.filter(id_agence=agence, statut="en cours").exists():
        data = Probleme.objects.filter(id_agence=agence, statut="en cours")
        for probleme in data:
            problemes.append({
                'Date de début': probleme.date_signalement.strftime('%d/%m/%Y'),
                'Agent ouverture': probleme.id_agent_ouverture.prenom + ' ' + probleme.id_agent_ouverture.nom,
                'Vehicule': probleme.id_vehicule.immatriculation,
                'Description': probleme.probleme
            })
    historique_ventes = []
    if Historique.objects.filter(id_agence=agence, id_statut=Statut.objects.get(statut="Vendu")).exists():
        data = Historique.objects.filter(id_agence=agence, id_statut=Statut.objects.get(statut="Vendu"))
        for h in data:
            historique_ventes.append({
                'Date de vente': h.date_debut.strftime('%d/%m/%Y'),
                'Nom du vendeur': h.id_agent.prenom + ' ' + h.id_agent.nom,
                'Véhicule': h.id_vehicule.immatriculation
            })
    if request.user.groups.filter(name="administrateur").exists():
        if request.method == "POST":
            if request.POST.get("nom"):
                agence.nom = request.POST.get("nom")
            if request.POST.get("adresse"):
                agence.adresse = request.POST.get("adresse")
            if request.POST.get("complement_adresse"):
                agence.complement_adresse = request.POST.get("complement_adresse")
            if request.POST.get("code_postal"):
                agence.code_postal = request.POST.get("code_postal")
            if request.POST.get("ville"):
                agence.ville = request.POST.get("ville")
            if request.POST.get("telephone"):
                agence.telephone = request.POST.get("telephone")
            if request.POST.get("fax"):
                agence.fax = request.POST.get("fax")
            agence.save()
            return render(request, '../templates/agence/ficheAgenceAdmin.html',
                          {'confirmation': True,
                           'agence': agence,
                           'agents': agents,
                           'problemes': problemes,
                           'historique_ventes': historique_ventes})
        return render(request, '../templates/agence/ficheAgenceAdmin.html',
                      {'agence': agence,
                       'agents': agents,
                       'problemes': problemes,
                       'historique_ventes': historique_ventes})
    else:
        return render(request, '../templates/agence/ficheAgenceUser.html',
                      {'agence': agence,
                       'agents': agents,
                       'problemes': problemes,
                       'historique_ventes': historique_ventes})


@login_required()
def supprimer(request, id_agence):
    if request.user.groups.filter(name="administrateur").exists():
        this_agence = Agence.objects.get(id=id_agence)
        agences = Agence.objects.all()
        agents = []
        if Agent.objects.filter(id_agence=this_agence).exists():
            agents = Agent.objects.filter(id_agence=this_agence)
        vehicules = []
        if Vehicule.objects.filter(id_agence=this_agence).exists():
            vehicules = Vehicule.objects.filter(id_agence=this_agence)
        if request.method == 'POST':
            # Réaffectation des agents dans d'autres agences :
            for agent in agents:
                if request.POST.get("agent_" + str(agent.id)):
                    agence = Agence.objects.get(nom=request.POST.get("agent_"+str(agent.id)))
                    agent.id_agence = agence
                    agent.save()
            # Réaffectation des véhicules dans d'autres agences :
            for vehicule in vehicules:
                if request.POST.get("vehicule_" + str(vehicule.id)):
                    agence = Agence.objects.get(nom=request.POST.get("vehicule_"+str(vehicule.id)))
                    vehicule.id_agence = agence
                    vehicule.save()
            this_agence.delete()
            return redirect('agences')
        return render(request, '../templates/agence/validationSuppressionAgence.html', {
            'this_agence': this_agence,
            'agences': agences,
            'agents': agents,
            'vehicules': vehicules
        })

