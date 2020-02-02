from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Agence


@login_required()
def generate(request):
    return render(request, '../templates/agences.html')


@login_required()
def ajouter_une_agence(request):
    if request.user.groups.filter(name="administrateur").exists():
        if request.method == "POST":
            nom = request.POST.get("nom")
            adresse = request.POST.get("adresse")
            complement_adresse = request.POST.get("complement_adresse")
            code_postal = request.POST.get("code_postal")
            ville = request.POST.get("ville")
            telephone = request.POST.get("telephone")
            fax = request.POST.get("fax")
            photo = request.POST.get("photo")
            new_agence = Agence(nom=nom, adresse=adresse, complement_adresse=complement_adresse, code_postal=code_postal, ville=ville, telephone=telephone, fax=fax, photo=photo)
            new_agence.save()
            # TODO : page agence avec message de confirmation d'enregistrement d'agence
            return redirect('confirmation_enregistrement_agence')
        return render(request, 'agence/ajouter_une_agence.html', locals())


@login_required()
def actuellement(request):
    if request.user.groups.filter(name="administrateur").exists():
        nombre_agences = Agence.objects.all().count()
        # TODO : véhicules vendus depuis le début + véhicules vendus le mois dernier
        # vehicules_vendus =
        # vehicules_vendus_mois_dernier =
        return render(request, 'agence/actuellement.html', {'nombre_agences': nombre_agences})


@login_required()
def rechercher_une_agence(request):
    agences = Agence.objects.all()
    # TODO : ajouter nb de personnes, nb de véhicules, problèmes en cours, nb de véhicules vendus, responsable de l'agence avec mail
    # nb_personnes =
    # nb_vehicules =
    # nb_problemes =
    # nb_vendus =
    # responsable_agence =
    # mail_responsable =
    return render(request, 'agence/rechercher_une_agence.html', {'agences': agences})


@login_required()
def fiche_agence(request, id_agence):
    agence = Agence.objects.get(id=id_agence)
    # TODO : ajouter problèmes sur véhicules de l'agence, historique des ventes de l'agence, liste du personnel de l'agence
    return render(request, 'agence/fiche_agence.html', {'agence': agence})


@login_required()
def supprimer_agence(request, id_agence):
    if request.user.groups.filter(name="administrateur").exists():
        agence = Agence.objects.get(id=id_agence)
        agence.delete()
        # TODO: ajouter un message de confirmation de suppression de l'agence
        return render(request, '../templates/agences.html')


@login_required()
def modifier_agence(request, id_agence):
    if request.user.groups.filter(name="administrateur").exists():
        agence = get_object_or_404(Agence, id=id_agence)
        if request.method == "POST":
            nom = request.POST.get("nom")
            adresse = request.POST.get("adresse")
            complement_adresse = request.POST.get("complement_adresse")
            code_postal = request.POST.get("code_postal")
            ville = request.POST.get("ville")
            telephone = request.POST.get("telephone")
            fax = request.POST.get("fax")
            photo = request.POST.get("photo")
            updated_agence = Agence(nom=nom, adresse=adresse, complement_adresse=complement_adresse, code_postal=code_postal, ville=ville, telephone=telephone, fax=fax, photo=photo)
            updated_agence.save()
            # TODO : page agence avec message de confirmation de mise à jour d'agence
            return redirect('confirmation_maj_agence')
        return render(request, 'agence/fiche_modifier_agence.html', {'agence': agence})


