from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Agence
from agent.models import Agent
from datetime import date


@login_required()
def generate(request):
    identifiant = request.user.username
    agent = Agent.objects.get(identifiant=identifiant)
    # Pour le tableau :
    agences = Agence.objects.all()
    agences_table = []
    for item in agences:
        agences_table.append({
            'Ville': item.ville,
            'Agence': item.nom,
            'Nb_de_vehicules': '',
            'Probleme_en_cours': '',
            'Vehicules_vendus': '',
            'Responsable_de_l_agence': '',
            'Telephone': item.telephone,
            'Mail': '',
            'Vue': ''
        })
    # TODO : ajouter nb de personnes, nb de véhicules, problèmes en cours, nb de véhicules vendus, responsable de l'agence avec mail
    # nb_personnes =
    # nb_vehicules =
    # nb_problemes =
    # nb_vendus =
    # responsable_agence =
    # mail_responsable =
    # Admin :
    if request.user.groups.filter(name="administrateur").exists():
        #  Pour le carré actuellement
        # TODO : véhicules vendus depuis le début + véhicules vendus le mois dernier
        # vehicules_vendus =
        # vehicules_vendus_mois_dernier =
        # total_vehicules =
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
                               'agences_table': str(agences_table),
                               'this_year': this_year,
                               'this_month': this_month})
            else:
                return render(request,
                              '../templates/agence/agenceAdmin.html',
                              {'error': True,
                               'agent': agent,
                               'nombre_agences': nombre_agences,
                               'agences_table': str(agences_table),
                               'this_year': this_year,
                               'this_month': this_month})
        else:
            return render(request,
                          '../templates/agence/agenceAdmin.html',
                          {'error': False,
                           'confirmation': False,
                           'agent': agent,
                           'nombre_agences': nombre_agences,
                           'agences_table': str(agences_table),
                           'this_year': this_year,
                           'this_month': this_month})
    else:
        # USER :
        return render(request, '../templates/agence/agenceUser.html', {'agent': agent, 'agences_table': str(agences_table)})


@login_required()
def fiche(request, id_agence):
    agence = Agence.objects.get(id=id_agence)
    return render(request, '../templates/agence/fiche_agence.html', {'agence': agence})


# @login_required()
# def actuellement(request):
#     if request.user.groups.filter(name="administrateur").exists():
#         nombre_agences = Agence.objects.all().count()
#         # TODO : véhicules vendus depuis le début + véhicules vendus le mois dernier
#         # vehicules_vendus =
#         # vehicules_vendus_mois_dernier =
#         return render(request, 'agence/actuellement.html', {'nombre_agences': nombre_agences})


# @login_required()
# def rechercher_une_agence(request):
#     agences = Agence.objects.all()
#     # TODO : ajouter nb de personnes, nb de véhicules, problèmes en cours, nb de véhicules vendus, responsable de l'agence avec mail
#     # nb_personnes =
#     # nb_vehicules =
#     # nb_problemes =
#     # nb_vendus =
#     # responsable_agence =
#     # mail_responsable =
#     return render(request, 'agence/rechercher_une_agence.html', {'agences': agences})


# @login_required()
# def fiche_agence(request, id_agence):
#     agence = Agence.objects.get(id=id_agence)
#     # TODO : ajouter problèmes sur véhicules de l'agence, historique des ventes de l'agence, liste du personnel de l'agence
#     return render(request, 'agence/fiche_agence.html', {'agence': agence})
#
#
# @login_required()
# def supprimer_agence(request, id_agence):
#     if request.user.groups.filter(name="administrateur").exists():
#         agence = Agence.objects.get(id=id_agence)
#         agence.delete()
#         # TODO: ajouter un message de confirmation de suppression de l'agence
#         return render(request, '../templates/agences.html')
#
#
# @login_required()
# def modifier_agence(request, id_agence):
#     if request.user.groups.filter(name="administrateur").exists():
#         agence = get_object_or_404(Agence, id=id_agence)
#         if request.method == "POST":
#             nom = request.POST.get("nom")
#             adresse = request.POST.get("adresse")
#             complement_adresse = request.POST.get("complement_adresse")
#             code_postal = request.POST.get("code_postal")
#             ville = request.POST.get("ville")
#             telephone = request.POST.get("telephone")
#             fax = request.POST.get("fax")
#             photo = request.POST.get("photo")
#             updated_agence = Agence(nom=nom, adresse=adresse, complement_adresse=complement_adresse, code_postal=code_postal, ville=ville, telephone=telephone, fax=fax, photo=photo)
#             updated_agence.save()
#             # TODO : page agence avec message de confirmation de mise à jour d'agence
#             return redirect('confirmation_maj_agence')
#         return render(request, 'agence/fiche_modifier_agence.html', {'agence': agence})


