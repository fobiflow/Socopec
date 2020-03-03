from django.contrib.auth.models import User, Group
from django.http import HttpResponse
from django.template import loader
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
            'm': '<a href="modifierAdmin/' + str(item.id) + '"><img alt="modification agent" class="icon" src="../../../static/images/modifier.svg"/></a>',
            's': '<a href="supprimer/' + str(item.id) + '"><img alt="suppression agent" class="icon" src="../../../static/images/supprimer.svg"/></a>'
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
                    context = {'errorShortPw': True,
                               'agent': agent,
                               'total': total,
                               'femmes': femmes,
                               'hommes': hommes,
                               'agents_table': agents_table,
                               'options': options}
                    template = loader.get_template('../templates/agent/agentAdmin.html')
                    return HttpResponse(template.render(context, request))
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
                        photo="https://cdn.pixabay.com/photo/2016/08/31/11/54/user-1633249_960_720.png",
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
                            's': '<a href="/supprimer/' + str(item.id) + '"><img alt="acces fiche agence" class="icon" src="../../../static/images/supprier.svg"/></a>'
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
            #  TODO : clôturer les problèmes / historique en cours pour cet agent
            agent.delete()
            return redirect('agents')
        return render(request, '../templates/agent/validationSuppressionAgent.html', {'agent': agent})


@login_required
def modifier_admin(request, id_agent):
    agent = Agent.objects.get(id=id_agent)
    options = []
    agences = Agence.objects.all()
    for item in agences:
        options.append(item.nom)
    if request.method == "POST":
        user = User.objects.get(username=agent.identifiant)
        if request.POST.get("poste_socopec"):
            if request.POST.get("poste_socopec") == "Administrateur" or request.POST.get(
                    "poste_socopec") == "administrateur":
                group_user = Group.objects.get(name="utilisateur")
                group_user.user_set.remove(user)
                group_admin = Group.objects.get(name="administrateur")
                group_admin.user_set.add(user)
            else:
                group = Group.objects.get(name="utilisateur")
                group.user_set.add(user)

        if request.POST.get("nom"):
            agent.nom = request.POST.get("nom")
        if request.POST.get("prenom"):
            agent.prenom = request.POST.get("prenom")
        if request.POST.get("email"):
            agent.email = request.POST.get("email")
        if request.POST.get("poste_socopec"):
            agent.poste_socopec = request.POST.get("poste_socopec")
        # TODO : corriger erreur de format de date pour modifications
        if request.POST.get("date_entree_socopec"):
            agent.date_entree_socopec = request.POST.get("date_entree_socopec")
        if request.POST.get("agence"):
            agent.id_agence = Agence.objects.get(nom=request.POST.get("agence"))
        agent.save()
        return render(request, '../templates/agent/modifierAgentAdmin.html', {'agent': agent, 'options': options, 'validation': True})
    return render(request, '../templates/agent/modifierAgentAdmin.html', {'agent': agent, 'options': options})


@login_required
def modifier(request):
    identifiant = request.user.username
    agent = Agent.objects.get(identifiant=identifiant)
    options = []
    agences = Agence.objects.all()
    for item in agences:
        options.append(item.nom)
    if request.method == "POST":
        if request.POST.get("mot_de_passe"):
            if len(request.POST.get("mot_de_passe")) < 8:
                context = {'errorShortPw': True, 'agent': agent, 'options': options}
                template = loader.get_template('../templates/agent/compte.html')
                return HttpResponse(template.render(context, request))
            if request.POST.get("confirmation_mot_de_passe") and request.POST.get("mot_de_passe") != request.POST.get("confirmation_mot_de_passe"):
                form = request.POST.get(all)
                context = {'form': form, 'errorPw': True, 'agent': agent, 'options': options}
                template = loader.get_template('../templates/agent/compte.html')
                return HttpResponse(template.render(context, request))

        if request.POST.get("adresse") and request.POST.get("adresse") != agent.adresse:
            agent.adresse = request.POST.get("adresse")
        if request.POST.get("complement_adresse") and request.POST.get("complement_adresse") != agent.complement_adresse:
            agent.complement_adresse = request.POST.get("complement_adresse")
        if request.POST.get("code_postal") and request.POST.get("code_postal") != agent.code_postal:
            agent.code_postal = request.POST.get("code_postal")
        if request.POST.get("ville") and request.POST.get("ville") != agent.ville:
            agent.ville = request.POST.get("ville")
        if request.POST.get("tel") and request.POST.get("tel") != agent.tel:
            agent.tel = request.POST.get("tel")
        if request.POST.get("mobile") and request.POST.get("mobile") != agent.mobile:
            agent.mobile = request.POST.get("mobile")
        if request.POST.get("email") and request.POST.get("email") != agent.email:
            agent.email = request.POST.get("email")
        if request.POST.get("identifiant") and request.POST.get("identifiant") != agent.identifiant:
            agent.identifiant = request.POST.get("identifiant")
        if request.POST.get("mot_de_passe") and request.POST.get("mot_de_passe") != agent.mot_de_passe:
            agent.mot_de_passe = request.POST.get("mot_de_passe")
        if request.POST.get("photo") and request.POST.get("photo") != agent.photo:
            agent.photo = request.POST.get("photo")
        agent.save()
        return render(request, '../templates/agent/compte.html', {'agent': agent})
    return render(request, '../templates/agent/compte.html', {'agent': agent, 'options': options})



