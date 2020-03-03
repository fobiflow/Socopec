from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Statut, Historique
from vehicule.models import Vehicule
from agence.models import Agence
from agent.models import Agent


@login_required
def creerHisto(request, id_vehicule):
    agences = []
    res_agences = Agence.objects.all()
    for item in res_agences:
        agences.append(item.nom)
    agents = Agent.objects.all()
    vehicule = Vehicule.objects.get(id=id_vehicule)
    identifiant = request.user.username
    agent = Agent.objects.get(identifiant=identifiant)
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
            ancien_histo = Historique.objects.get(id_vehicule=id_vehicule, statut="en cours")
            ancien_histo.statut = "terminé"
            ancien_histo.save()
            new_histo.save()
            return redirect('fiche_vehicule', id_vehicule=id_vehicule)
        else:
            return render(request, '../templates/historique/new_historique.html',
                          {'error': True,
                           'agences': agences,
                           'agents': agents,
                           'vehicule': vehicule,
                           'agent': agent,
                           'statuts': statuts
                           })
    return render(request, '../templates/historique/new_historique.html',
                  {'agences': agences,
                   'agents': agents,
                   'vehicule': vehicule,
                   'agent': agent,
                   'statuts': statuts})


@login_required
def updateHisto(request, id_historique):
    agences = []
    res_agences = Agence.objects.all()
    for item in res_agences:
        agences.append(item.nom)
    agents = Agent.objects.all()
    identifiant = request.user.username
    agent = Agent.objects.get(identifiant=identifiant)
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

# def lister(request):
#     return render(request, 'historique/lister.html')
#
#
# def creer(request):
#     return render(request, 'historique/creer.html')
#
#
# def modifier(request, id_historique):
#     return render(request, 'historique/modifier.html', locals())
#
#
# def supprimer(request, id_historique):
#     return render(request, 'historique/supprimer.html', locals())
#
#
# def voir(request, id_historique):
#     return render(request, 'historique/voir.html', locals())

