from django.contrib.auth.models import User, Group
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Agent
from agence.models import Agence

@login_required
def generate(request):
    identifiant = request.user.username
    agent = Agent.objects.get(identifiant=identifiant)
    # Pour le tableau :
    data = Agent.objects.all()
    agents_table = []

    for item in data:
        # agence = Agence.objects.filter()[:int(item.id_agence)]
        # for agence in agences:
        #     if agence.id == item.id_agence:
        #         agence_nom = agence.nom
        agents_table.append({
            'Agence': Agence.objects.get(id=item.id_agence.id).nom,
            'Fonction': item.poste_socopec,
            'Depuis': str(item.date_entree_socopec),
            'Nom': item.nom,
            'Prenom': item.prenom,
            'Email pro': item.email,
            'm': '<img alt="acces fiche agence" class="icon" src="../../../static/images/modifier.svg"/>',
            's': '<img alt="acces fiche agence" class="icon" src="../../../static/images/supprimer.svg"/>'
        })

    # Vue pour Admin :
    if request.user.groups.filter(name="administrateur").exists():
        # Pour le carré parité :
        total = data.count()
        femmes = Agent.objects.filter(sexe="F").count()
        hommes = Agent.objects.filter(sexe="H").count()

        # Pour le formulaire :
        options = []
        agences = Agence.objects.all()
        for item in agences:
            options.append(item.nom)
        if request.method == 'POST':
            if request.POST.get("nom") and \
                request.POST.get("prenom") and \
                request.POST.get("sexe") and \
                request.POST.get("adresse") and \
                request.POST.get("code_postal") and \
                request.POST.get("ville") and \
                request.POST.get("tel") and \
                request.POST.get("email") and \
                request.POST.get("date_entree_socopec") and \
                request.POST.get("poste_socopec") and \
                request.POST.get("identifiant") and \
                request.POST.get("mot_de_passe") and \
                request.POST.get("agence"):
                if len(request.POST.get("mot_de_passe")) < 8:
                    errPassword = True
                    return HttpResponseRedirect('', errPassword)
                else:
                    #  Création de l'agent pour Django Admin et attribution du bon groupe :
                    user = User.objects.create_user(request.POST.get("identifiant"), request.POST.get("email"),
                                                    request.POST.get("mot_de_passe"))
                    user.save()
                    if (request.POST.get("poste_socopec") == "Administrateur") or (request.POST.get("poste_socopec") == "administrateur"):
                        admin = True
                        group = Group.objects.get(name="administrateur")
                        group.user_set.add(user)
                    else:
                        admin = False
                        group = Group.objects.get(name="utilisateur")
                        group.user_set.add(user)
                    #     Création de l'utilisateur Agent dans la bdd :
                    agence = Agence.objects.get(nom=request.POST.get("agence"))
                    new_agent = Agent(
                        nom=request.POST.get("nom"),
                        prenom=request.POST.get("prenom"),
                        sexe=request.POST.get("sexe"),
                        adresse=request.POST.get("adresse"),
                        complement_adresse=request.POST.get("complement_adresse"),
                        code_postal=request.POST.get("code_postal"),
                        ville=request.POST.get("ville"),
                        tel=request.POST.get("tel"),
                        fax=request.POST.get("fax"),
                        mobile=request.POST.get("mobile"),
                        email=request.POST.get("email"),
                        date_entree_socopec=request.POST.get("date_entree_socopec"),
                        poste_socopec=request.POST.get("poste_socopec"),
                        admin=admin,
                        identifiant=request.POST.get("identifiant"),
                        mot_de_passe=request.POST.get("mot_de_passe"),
                        photo="",
                        id_agence=agence
                    )
                    new_agent.save()
                    total = Agent.objects.all().count()
                    femmes = Agent.objects.filter(sexe="F").count()
                    hommes = Agent.objects.filter(sexe="H").count()
                    data = Agent.objects.all()
                    agents_table = []
                    for item in data:
                        # agence = Agence.objects.filter()[:int(item.id_agence)]
                        # for agence in agences:
                        #     if agence.id == item.id_agence:
                        #         agence_nom = agence.nom
                        agents_table.append({
                            # 'Agence': agence.nom,
                            'Fonction': item.poste_socopec,
                            'Depuis': str(item.date_entree_socopec),
                            'Nom': item.nom,
                            'Prenom': item.prenom,
                            'Email pro': item.email,
                            'm': '<img alt="acces fiche agence" class="icon" src="../../../static/images/modifier.svg"/>',
                            's': '<img alt="acces fiche agence" class="icon" src="../../../static/images/supprimer.svg"/>'
                        })
                    return render(request, '../templates/agent/agentAdmin.html',
                                  {'error': False,
                                   'confirmation': True,
                                   'confirmation_firstname': request.POST.get('prenom'),
                                   'confirmation_name': request.POST.get('nom'),
                                   'agent': agent,
                                   'total': total,
                                   'femmes': femmes,
                                   'hommes': hommes,
                                   'agents_table': agents_table,
                                   'options': options
                                   })
            else:
                return render(request, '../templates/agent/agentAdmin.html',
                              {'error': True,
                               'confirmation': False,
                               'agent': agent,
                               'total': total,
                               'femmes': femmes,
                               'hommes': hommes,
                               'agents_table': agents_table,
                               'options': options
                               })
        else:
            return render(request, '../templates/agent/agentAdmin.html',
                          {'error': False,
                           'confirmation': False,
                           'agent': agent,
                           'total': total,
                           'femmes': femmes,
                           'hommes': hommes,
                           'agents_table': agents_table,
                           'options': options
                           })
    else:
        # USER
        return render(request, '../templates/agent/agentUser.html', {'agent': agent, 'agents_table': agents_table})


@login_required
def supprimer(request, id_agent):
    if request.user.groups.filter(name="administrateur").exists():
        agent = Agent.objects.get(id=id_agent)
        if request.method == 'POST':
            agent.delete()
            return redirect('agents')
        return render(request, '../templates/agent/validationSuppressionAgent.html', {'agent': agent})


@login_required
def modifier(request, id_agent):
    agent = get_object_or_404(Agent, id=id_agent)
    options = []
    agences = Agence.objects.all()
    for item in agences:
        options.append(item.nom)
    if request.method == "POST":
        user = User.objects.get(identifiant=agent.identifiant)
        if request.POST.get("poste_socopec") == "Administrateur" or request.POST.get("poste_socopec") == "administrateur":
            group = Group.objects.get(name="administrateur")
            group.user_set.add(user)
        else:
            group = Group.objects.get(name="utilisateur")
            group.user_set.add(user)
        agent.nom = request.POST.get("nom")
        agent.prenom = request.POST.get("prenom")
        agent.sexe = request.POST.get("sexe")
        agent.adresse = request.POST.get("adresse")
        agent.complement_adresse = request.POST.get("complement_adresse")
        agent.code_postal = request.POST.get("code_postal")
        agent.ville = request.POST.get("ville")
        agent.tel = request.POST.get("tel")
        agent.fax = request.POST.get("fax")
        agent.mobile = request.POST.get("mobile")
        agent.email = request.POST.get("email")
        agent.date_entree_socopec = request.POST.get("date_entree_socopec")
        agent.poste_socopec = request.POST.get("poste_socopec")
        agent.admin = request.POST.get("admin")
        agent.identifiant = request.POST.get("identifiant")
        agent.mot_de_passe = request.POST.get("mot_de_passe")
        agent.photo = request.POST.get("photo")
        agent.id_agence = Agence.objects.get(nom=request.POST.get("agence")).id
        agent.save()
        return render(request, '../templates/agent/compte.html', {'agent': agent})
    return render(request, '../templates/agent/compte.html', {'agent': agent, 'options': options})



