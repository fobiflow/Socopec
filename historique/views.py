from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Statut, Historique
from vehicule.models import Vehicule
from agence.models import Agence
from agent.models import Agent


@login_required
def creerHisto(request, id_vehicule):
    identifiant = request.user.username
    agent = Agent.objects.get(identifiant=identifiant)
    agences = []
    res_agences = Agence.objects.all()
    for item in res_agences:
        agences.append(item.nom)
    agents = Agent.objects.all()
    vehicule = Vehicule.objects.get(id=id_vehicule)
    statuts = []
    res_statuts = Statut.objects.all()
    for item in res_statuts:
        statuts.append(item.statut)
    if request.method == 'POST':
        if request.POST.get('date_debut') and request.POST.get('localisation'):
            if request.POST.get("date_fin"):
                new_histo = Historique(
                    id_agence=Agence.objects.get(nom=request.POST.get("agence")),
                    id_vehicule=Vehicule.objects.get(id=id_vehicule),
                    id_statut=Statut.objects.get(statut=request.POST.get("statut")),
                    id_agent=Agent.objects.get(id=request.POST.get("agent")),
                    date_debut=request.POST.get("date_debut"),
                    date_fin=request.POST.get("date_fin"),
                    localisation=request.POST.get("localisation")
                )
            else:
                new_histo = Historique(
                    id_agence=Agence.objects.get(nom=request.POST.get("agence")),
                    id_vehicule=Vehicule.objects.get(id=id_vehicule),
                    id_statut=Statut.objects.get(statut=request.POST.get("statut")),
                    id_agent=Agent.objects.get(id=request.POST.get("agent")),
                    date_debut=request.POST.get("date_debut"),
                    localisation=request.POST.get("localisation")
                )
            if Historique.objects.filter(id_vehicule=id_vehicule, statut="en cours").exists():
                ancien_histo = Historique.objects.get(id_vehicule=id_vehicule, statut="en cours")
                ancien_histo.statut = "terminé"
                ancien_histo.save()
            new_histo.save()
            return redirect('fiche_vehicule', id_vehicule=id_vehicule)
        else:
            return render(request, '../templates/historique/new_historique.html',
                          {'error': True,
                           'agences': agences,
                           'agent': agent,
                           'agents': agents,
                           'vehicule': vehicule,
                           'statuts': statuts
                           })
    return render(request, '../templates/historique/new_historique.html',
                  {'agences': agences,
                   'agents': agents,
                   'agent': agent,
                   'vehicule': vehicule,
                   'statuts': statuts})


@login_required
def updateHisto(request, id_historique):
    agences = []
    res_agences = Agence.objects.all()
    for item in res_agences:
        agences.append(item.nom)
    agents = Agent.objects.all()
    historique = Historique.objects.get(id=id_historique)
    statuts = []
    res_statuts = Statut.objects.all()
    for item in res_statuts:
        statuts.append(item.statut)
    if request.method == 'POST':
        if request.POST.get("agence") != historique.id_agence.nom:
            historique.id_agence = Agence.objects.get(nom=request.POST.get("agence"))
        if request.POST.get("agent") != historique.id_agent:
            historique.id_agent = Agent.objects.get(id=request.POST.get("agent"))
        if request.POST.get("statut") != historique.id_statut.statut:
            historique.id_statut = Statut.objects.get(statut=request.POST.get("statut"))
        if request.POST.get("date_debut"):
            historique.date_debut = request.POST.get("date_debut")
        if request.POST.get("date_fin"):
            historique.date_fin = request.POST.get("date_fin")
        if request.POST.get("localisation"):
            historique.localisation = request.POST.get("localisation")
        historique.save()
        return redirect('fiche_vehicule', id_vehicule=historique.id_vehicule.id)
    return render(request, '../templates/historique/update_historique.html', {'agences': agences, 'agents': agents, 'statuts': statuts, 'historique': historique})


@login_required
def creerStatut(request):
    if request.user.groups.filter(name="administrateur").exists():
        if request.method == 'POST':
            statuts = Statut.objects.all()
            if request.POST.get("statut"):
                new_statut = Statut(
                    statut=request.POST.get("statut")
                )
                plusDeDix = False
                if Statut.objects.all().count() > 9:
                    plusDeDix = True
                if plusDeDix == True:
                    return render(request, '../templates/historique/nouveau_statut.html', {'plusDeDix': True})
                else:
                    error = False
                    for item in statuts:
                        if item.statut == request.POST.get("statut"):
                            error = True
                    if error == True:
                        return render(request, '../templates/historique/nouveau_statut.html', {'error': True})
                    else:
                        new_statut.save()
                        return redirect('vehicules')
        return render(request, '../templates/historique/nouveau_statut.html')


@login_required
def updateStatut(request, id_statut):
    if request.user.groups.filter(name="administrateur").exists():
        statut=Statut.objects.get(id=id_statut)
        if request.POST.get("statut"):
            statuts = Statut.objects.all()
            error = False
            for item in statuts:
                if item.statut == request.POST.get("statut"):
                    error = True
            if error == True:
                return render(request, '../templates/historique/update_statut.html', {'error': True})
            else:
                statut.statut = request.POST.get("statut")
                statut.save()
                return redirect('vehicules')
        return render(request, '../templates/historique/update_statut.html', {'statut': statut})


@login_required
def deleteStatut(request, id_statut):
    if request.user.groups.filter(name="administrateur").exists():
        statut=Statut.objects.get(id=id_statut)
        return render(request, '../templates/historique/delete_statut.html', {'statut': statut})
