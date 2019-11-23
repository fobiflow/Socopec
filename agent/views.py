from django.shortcuts import render, redirect, get_object_or_404
from .forms import AgentForm
from .models import Agent


def lister(request):
    agents = Agent.objects.all()
    return render(request, 'agent/lister.html', {'agents': agents})


def creer(request):
    if request.POST:
        form = AgentForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('lister_agent')
    else:
        form = AgentForm()
    return render(request, 'agent/creer.html', {'form': form})


def modifier(request, id_agent):
    agent = get_object_or_404(Agent, id=id_agent)
    form = AgentForm(request.POST or None, instance=agent)
    if form.is_valid():
        form.save()
        return redirect('lister_agent')
    return render(request, 'agent/modifier.html', {'form': form, 'id_agent': id_agent})


def supprimer(request, id_agent):
    agent = Agent.objects.get(id=id_agent)
    agent.delete()
    return render(request, 'agent/supprimer.html', locals())


def voir(request, id_agent):
    agent = Agent.objects.get(id=id_agent)
    return render(request, 'agent/voir.html', {'agent': agent})

