from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from historique.models import Probleme
from vehicule.models import Vehicule
from agence.models import Agence
from agent.models import Agent
import datetime

@login_required
def creerProbleme(request, id_vehicule):
    agences = []
    res_agences = Agence.objects.all()
    for item in res_agences:
        agences.append(item.nom)
    agents = Agent.objects.all()
    vehicule = Vehicule.objects.get(id=id_vehicule)
    if request.method == 'POST':
        if request.POST.get("probleme"):
            if request.POST.get("date_signalement"):
                new_probleme = Probleme(
                    id_vehicule=Vehicule.objects.get(id=id_vehicule),
                    id_agence=Agence.objects.get(nom=request.POST.get("agence")),
                    id_agent_ouverture=Agent.objects.get(id=request.POST.get("agent_ouverture")),
                    probleme=request.POST.get("probleme"),
                    statut="en cours",
                    date_signalement=request.POST.get("date_signalement")
                )
            else:
                new_probleme = Probleme(
                    id_vehicule=Vehicule.objects.get(id=id_vehicule),
                    id_agence=Agence.objects.get(nom=request.POST.get("agence")),
                    id_agent_ouverture=Agent.objects.get(id=request.POST.get("agent_ouverture")),
                    probleme=request.POST.get("probleme"),
                    statut="en cours"
                )
            new_probleme.save()
            return redirect('fiche_vehicule', id_vehicule=id_vehicule)
        else:
            return render(request, '../templates/probleme/new_probleme.html', {
                'error': True,
                'agences': agences,
                'agents': agents,
                'vehicule': vehicule})
    return render(request, '../templates/probleme/new_probleme.html',
                  {'agences': agences,
                   'agents': agents,
                   'vehicule': vehicule})


@login_required
def updateProbleme(request, id_probleme):
    agences = []
    res_agences = Agence.objects.all()
    for item in res_agences:
        agences.append(item.nom)
    agents = Agent.objects.all()
    probleme = Probleme.objects.get(id=id_probleme)
    if request.method == 'POST':
        if request.POST.get("agence") != probleme.id_agence.nom:
            probleme.id_agence = Agence.objects.get(nom=request.POST.get("agence"))
        if request.POST.get("agent_ouverture") != probleme.id_agent_ouverture.id:
            probleme.id_agent_ouverture = Agent.objects.get(id=request.POST.get("agent_ouverture"))
        if request.POST.get("probleme"):
            probleme.probleme = request.POST.get("probleme")
        if request.POST.get("date_signalement"):
            probleme.date_signalement = request.POST.get("date_signalement")
        probleme.save()
        return redirect('fiche_vehicule', id_vehicule=probleme.id_vehicule.id)
    return render(request, '../templates/probleme/update_probleme.html',
                  {'agences': agences,
                   'agents': agents,
                   'probleme': probleme})


@login_required
def closeProbleme(request, id_probleme):
    agents = Agent.objects.all()
    identifiant = request.user.username
    agent = Agent.objects.get(identifiant=identifiant)
    probleme = Probleme.objects.get(id=id_probleme)
    date_ouverture = probleme.date_signalement.strftime("%d/%m/%Y")
    if request.method == 'POST':
        probleme.agent_resolution = request.POST.get("agent_resolution")
        if request.POST.get("date_resolution"):
            probleme.date_resolution = request.POST.get("date_resolution")
        else:
            probleme.date_resolution = datetime.date.today()
        probleme.statut = "terminé"
        probleme.save()
        return redirect('fiche_vehicule', id_vehicule=probleme.id_vehicule.id)
    return render(request, '../templates/probleme/close_probleme.html',
                  {'agents': agents,
                   'agent': agent,
                   'date_ouverture': date_ouverture,
                   'probleme': probleme})
