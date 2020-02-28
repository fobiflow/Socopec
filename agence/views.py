from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Agence
from agent.models import Agent
from vehicule.models import Vehicule
from datetime import date


@login_required()
def generate(request):
    identifiant = request.user.username
    agent = Agent.objects.get(identifiant=identifiant)

    # Pour le tableau :
    data = Agence.objects.all()
    agences_table = []
    for item in data:
        agences_table.append({
            'Ville': item.ville,
            'Agence': item.nom,
            'Nb de personne': '',
            'Nb de vehicules': Vehicule.objects.filter(id_agence=item.id).count(),
            'Probleme en cours': '',
            'Vehicules vendus': '',
            'Responsable de l\'agence': '',
            'Telephone': item.telephone,
            'Mail': '',
            'Vue': '<a href="' + str(item.id) + '"><img alt="acces fiche agence" class="icon" src="../../../static/images/oeuil.svg"/></a>'
        })

    # Vue pour admin :
    if request.user.groups.filter(name="administrateur").exists():
        #  Pour le carré actuellement
        # TODO : véhicules vendus depuis le début + véhicules vendus le mois dernier
        # vehicules_vendus =
        # vehicules_vendus_mois_dernier =
        total_vehicules = Vehicule.objects.all().count()
        this_year = date.today().year
        int_month = date.today().month
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
            # TODO : message de confirmation de mise à jour d'agence

            return redirect('fiche_agence', id_agence=agence.id)
        return render(request, '../templates/agence/ficheAgenceAdmin.html', {'agence': agence, 'agents': agents})
    else:
        return render(request, '../templates/agence/ficheAgenceUser.html', {'agence': agence, "agents": agents})


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

