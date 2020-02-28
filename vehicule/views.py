from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Vehicule, Photo
from agent.models import Agent
from agence.models import Agence
import locale
locale.setlocale(locale.LC_TIME, '')
import time


@login_required
def generate(request):
    identifiant = request.user.username
    agent = Agent.objects.get(identifiant=identifiant)
    data = Vehicule.objects.all()
    vehicules_table = []
    # TODO : ajout d'une couleur en fonction de l'historique (problème urgent ou pas, à revoir avec Laurence)
    # TODO 2 : ajout du statut, de la localisation et des dates
    for item in data:
       vehicules_table.append({
           'P': '',
           'Plaque': item.immatriculation,
           'Agence': item.id_agence.nom,
           'Modèle': item.modele,
           'Statut': '',
           'Localisation': '',
           'Dates': '',
           'Date de fab.': str(item.date_fabrication),
           'CV': item.puissance,
           'Poids': item.poids,
           'H': item.hauteur,
           'L': item.largeur,
           'o': '<a href="' + str(item.id) + '"><img alt="acces fiche vehicule" class="icon" src="../../../static/images/oeuil.svg"/></a>',
           'x': ''
       })
    # Vue pour Admin :
    if request.user.groups.filter(name="administrateur").exists():
        date = time.strftime('%A %d-%m-%Y')
        # Pour les stats :
        total_vehicules = data.count()
        #  TODO : ajouter les problèmes et nombre de véhicules en fonction du statut pour les barres de progression
        problemes_orange = 0
        problemes_rouge = 0
        if request.method == 'POST':
            if request.POST.get('agence') and \
                request.POST.get('immatriculation') and \
                request.POST.get('modele') and \
                request.POST.get('etat') and \
                request.POST.get('date_fabrication') and \
                request.POST.get('puissance') and \
                request.POST.get('poids') and \
                request.POST.get('hauteur'):
                new_vehicule = Vehicule(
                    immatriculation=request.POST.get('immatriculation'),
                    modele=request.POST.get('modele'),
                    date_fabrication=request.POST.get('date_fabrication'),
                    hauteur=request.POST.get('hauteur'),
                    largeur=request.POST.get('largeur'),
                    poids=request.POST.get('poids'),
                    puissance=request.POST.get('puissance'),
                    id_agence=Agence.objects.get(nom=request.POST.get('agence'))
                )
                new_vehicule.save()
                # TODO : ajouter les photos à la table photo en split un seul retour à chaque virgule
                if request.POST.get('photo_1'):
                    new_photo = Photo(
                        url=request.POST.get('photo_1'),
                        id_vehicule=Vehicule.objects.get(immatriculation=request.POST.get('immatriculation')).id
                    )
                    new_photo.save()
                if request.POST.get('photo_2'):
                    new_photo = Photo(
                        url=request.POST.get('photo_2'),
                        id_vehicule=Vehicule.objects.get(immatriculation=request.POST.get('immatriculation')).id
                    )
                    new_photo.save()
                if request.POST.get('photo_3'):
                    new_photo = Photo(
                        url=request.POST.get('photo_3'),
                        id_vehicule=Vehicule.objects.get(immatriculation=request.POST.get('immatriculation')).id
                    )
                    new_photo.save()
                return render(request, '../templates/vehicule/vehiculeAdmin.html',
                              {'error': False,
                               'confirmation': True,
                               'agent': agent,
                               'total_vehicules': total_vehicules,
                               'problemes_orange': problemes_orange,
                               'problemes_rouge': problemes_rouge,
                               'date': date,
                               'data': data,
                               'vehicules_table': vehicules_table})
            else:
                return render(request, '../templates/vehicule/vehiculeAdmin.html',
                              {'error': True,
                               'confirmation': False,
                               'agent': agent,
                               'total_vehicules': total_vehicules,
                               'problemes_orange': problemes_orange,
                               'problemes_rouge': problemes_rouge,
                               'date': date,
                               'data': data,
                               'vehicules_table': vehicules_table})
        else:
            return render(request, '../templates/vehicule/vehiculeAdmin.html',
                          {'error': False,
                           'confirmation': False,
                           'agent': agent,
                           'total_vehicules': total_vehicules,
                           'problemes_orange': problemes_orange,
                           'problemes_rouge': problemes_rouge,
                           'date': date,
                           'data': data,
                           'vehicules_table': vehicules_table})
    # Vue pour User :
    return render(request, '../templates/vehicule/vehiculeUser.html', {'agent': agent, 'vehicules_table': vehicules_table})


@login_required()
def fiche(request, id_vehicule):
    vehicule = Vehicule.objects.get(id=id_vehicule)
    if request.user.groups.filter(name="administrateur").exists():
        if request.method == 'POST':
            if request.POST.get('immatriculation'):
                vehicule.immatriculation = request.POST.get('immatriculation')
            if request.POST.get('modele'):
                vehicule.modele = request.POST.get('modele')
            if request.POST.get('date_fabrication'):
                vehicule.date_fabrication = request.POST.get('date_fabrication')
            if request.POST.get('hauteur'):
                vehicule.hauteur = request.POST.get('hauteur')
            if request.POST.get('largeur'):
                vehicule.largeur = request.POST.get('largeur')
            if request.POST.get('poids'):
                vehicule.poids = request.POST.get('poids')
            if request.POST.get('puissance'):
                vehicule.puissance = request.POST.get('puissance')
            if request.POST.get('agence') != vehicule.id_agence.nom:
                vehicule.id_agence = Agence.objects.get(nom=request.POST.get('agence'))
            vehicule.save()
        #     TODO : message de confirmation de mise à jour du véhicule
        return render(request, '../templates/vehicule/ficheVehiculeAdmin.html', {'vehicule': vehicule})
    else:
        return render(request, '../templates/vehicule/ficheVehiculeUser.html', {'vehicule': vehicule})

@login_required()
def supprimer(request, id_vehicule):
    if request.user.groups.filter(name="administrateur").exists():
        vehicule = Vehicule.objects.get(id=id_vehicule)
        if request.method == 'POST':
            vehicule.delete()
            return redirect('vehicules')
        return render(request, '../templates/vehicule/confirmationSuppressionVehicule.html',
                      {'vehicule': vehicule})
