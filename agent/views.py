from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Agent
from .models import Agence


@login_required
def generate(request):
    identifiant = request.user.username
    agent = Agent.objects.get(identifiant=identifiant)
    return render(request, '../templates/agents.html', {'agent': agent})


@login_required
def modifier_agents(request, id_agent):
    agent = get_object_or_404(Agent, id=id_agent)
    if request.method == "POST":
        nom = request.POST.get("nom")
        prenom = request.POST.get("prenom")
        sexe = request.POST.get("sexe")
        adresse = request.POST.get("adresse")
        complement_adresse = request.POST.get("complement_adresse")
        code_postal = request.POST.get("code_postal")
        ville = request.POST.get("ville")
        tel = request.POST.get("tel")
        fax = request.POST.get("fax")
        mobile = request.POST.get("mobile")
        email = request.POST.get("email")
        date_entree_socopec = request.POST.get("date_entree_socopec")
        poste_socopec = request.POST.get("poste_socopec")
        admin = request.POST.get("admin")
        identifiant = request.POST.get("identifiant")
        mot_de_passe = request.POST.get("mot_de_passe")
        photo = request.POST.get("photo")
        # TODO : récupération de l'id de l'agence
        id_agence = request.POST.get("agence")
        updated_agent = Agent(nom=nom, prenom=prenom, sexe=sexe, adresse=adresse, complement_adresse=complement_adresse,
                              code_postal=code_postal, ville=ville, tel=tel, fax=fax, mobile=mobile, email=email,
                              date_entree_socopec=date_entree_socopec, poste_socopec=poste_socopec, admin=admin,
                              identifiant=identifiant, mot_de_passe=mot_de_passe, photo=photo, id_agence=id_agence)
        updated_agent.save()
        # TODO : si l'identifiant ou le mot de passe ou le statut admin ont changé,
        #        modifier aussi l'entrée dans l'Admin de Django
        # TODO : page agence avec message de confirmation de mise à jour d'agence
        return redirect('confirmation_maj_agence')
    return render(request, 'agent/compte.html', {'agent': agent})


# def lister(request):
#     data['agents'] = Agent.objects.all()
#     data['agences'] = Agence.objects.all()
#     return render(request, 'agent/lister.html', {'data': data})
#
#
# def creer(request):
#     if request.POST:
#         form = AgentForm(request.POST)
#         if form.is_valid:
#             form.save()
#             return redirect('lister_agent')
#     else:
#         form = AgentForm()
#     return render(request, 'agent/creer.html', {'form': form})
#
#
# def modifier(request, id_agent):
#     agent = get_object_or_404(Agent, id=id_agent)
#     form = AgentForm(request.POST or None, instance=agent)
#     if form.is_valid():
#         form.save()
#         return redirect('lister_agent')
#     return render(request, 'agent/modifier.html', {'form': form, 'id_agent': id_agent})
#
#
# def supprimer(request, id_agent):
#     agent = Agent.objects.get(id=id_agent)
#     agent.delete()
#     return render(request, 'agent/supprimer.html', locals())
#
#
# def voir(request, id_agent):
#     agent = Agent.objects.get(id=id_agent)
#     return render(request, 'agent/voir.html', {'agent': agent})

