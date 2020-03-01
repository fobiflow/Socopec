from datetime import date

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Vehicule, Photo
from agent.models import Agent
from agence.models import Agence
from historique.models import Statut, Historique, Probleme
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
    color = "white"
    for item in data:
        if Probleme.objects.filter(statut="en cours").exists():
            color = "orange"
        if Probleme.objects.filter(statut="en cours", date_signalement__day=date.today().day).exists():
            color = "red"
        localisation = ""
        statut = ""
        dates = ""
        if Historique.objects.filter(id_vehicule=item, statut="en cours").exists():
            localisation = Historique.objects.get(id_vehicule=item, statut="en cours").localisation
            statut = Historique.objects.get(id_vehicule=item, statut="en cours").id_statut.statut
            if Historique.objects.get(id_vehicule=item, statut="en cours").date_fin:
                dates = str(Historique.objects.get(id_vehicule=item, statut="en cours").date_debut) + " au " + str(Historique.objects.get(id_vehicule=item, statut="en cours").date_fin)
            else:
                dates = str(Historique.objects.get(id_vehicule=item, statut="en cours").date_debut) + " au --/--/----"
        vehicules_table.append({
           'P': '<div style="width:10px;height:25px;background-color:' + color + '"></div>',
           'Plaque': item.immatriculation,
           'Agence': item.id_agence.nom,
           'Modèle': item.modele,
           'Statut': statut,
           'Localisation': localisation,
           'Dates': dates,
           'Date de fab.': str(item.date_fabrication),
           'CV': item.puissance,
           'Poids': item.poids,
           'H': item.hauteur,
           'L': item.largeur,
           'o': '<a href="' + str(item.id) + '"><img alt="acces fiche vehicule" class="icon" src="../../../static/images/oeuil.svg"/></a>',
        })
    # Vue pour Admin :
    if request.user.groups.filter(name="administrateur").exists():
        actu = time.strftime('%A %d-%m-%Y')
        # Pour les stats :
        total_vehicules = data.count()
        statuts = []
        res = Statut.objects.all()
        boots = ["", "bg-success", "bg-warning", "bg-danger", "bg-info"]
        i = 0
        for item in res:
            statuts.append({
                'statut': item.statut, 'value': Historique.objects.filter(id_statut=item.id).count(), "boots": boots[i]
            })
            i += 1
        problemes_orange = Probleme.objects.filter(statut="en cours").count()
        problemes_rouge = Probleme.objects.filter(date_signalement__day=date.today().day).count()
        options = []
        agences = Agence.objects.all()
        for item in agences:
            options.append(item.nom)
        if request.method == 'POST':
            if request.POST.get('agence') and \
                request.POST.get('immatriculation') and \
                request.POST.get('modele') and \
                request.POST.get('date_fabrication') and \
                request.POST.get('puissance') and \
                request.POST.get('poids') and \
                request.POST.get('hauteur') and \
                request.POST.get('largeur'):
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
                        id_vehicule=Vehicule.objects.get(immatriculation=request.POST.get('immatriculation'))
                    )
                    new_photo.save()
                if request.POST.get('photo_2'):
                    new_photo = Photo(
                        url=request.POST.get('photo_2'),
                        id_vehicule=Vehicule.objects.get(immatriculation=request.POST.get('immatriculation'))
                    )
                    new_photo.save()
                if request.POST.get('photo_3'):
                    new_photo = Photo(
                        url=request.POST.get('photo_3'),
                        id_vehicule=Vehicule.objects.get(immatriculation=request.POST.get('immatriculation'))
                    )
                    new_photo.save()
                return render(request, '../templates/vehicule/vehiculeAdmin.html',
                              {'error': False,
                               'confirmation': True,
                               'agent': agent,
                               'options': options,
                               'total_vehicules': total_vehicules,
                               'statuts': statuts,
                               'problemes_orange': problemes_orange,
                               'problemes_rouge': problemes_rouge,
                               'actu': actu,
                               'data': data,
                               'vehicules_table': vehicules_table})
            else:
                return render(request, '../templates/vehicule/vehiculeAdmin.html',
                              {'error': True,
                               'confirmation': False,
                               'agent': agent,
                               'options': options,
                               'total_vehicules': total_vehicules,
                               'statuts': statuts,
                               'problemes_orange': problemes_orange,
                               'problemes_rouge': problemes_rouge,
                               'actu': actu,
                               'data': data,
                               'vehicules_table': vehicules_table})
        else:
            return render(request, '../templates/vehicule/vehiculeAdmin.html',
                          {'error': False,
                           'confirmation': False,
                           'agent': agent,
                           'options': options,
                           'total_vehicules': total_vehicules,
                           'statuts': statuts,
                           'problemes_orange': problemes_orange,
                           'problemes_rouge': problemes_rouge,
                           'actu': actu,
                           'data': data,
                           'vehicules_table': vehicules_table})
    # Vue pour User :
    return render(request, '../templates/vehicule/vehiculeUser.html', {'agent': agent, 'vehicules_table': vehicules_table})


@login_required()
def fiche(request, id_vehicule):
    vehicule = Vehicule.objects.get(id=id_vehicule)
    photos = []
    if Photo.objects.filter(id_vehicule=vehicule).exists():
        ret = Photo.objects.filter(id_vehicule=vehicule)
        for item in ret:
            photos.append(item.url)
    historiques = Historique.objects.filter(id_vehicule=vehicule)
    historiques_table = []
    for item in historiques:
        if item.date_debut and item.date_fin:
            date = str(item.date_debut) + ' au ' + str(item.date_fin)
        else:
            date = str(item.date_debut) + ' au --/--/--'
        historiques_table.append({
            'Dates': date,
            'Statut': item.id_statut.statut,
            'Agence': item.id_agence.nom,
            'Agent': item.id_agent.prenom + ' ' + item.id_agent.nom,
            'M': '<a href="' + str(item.id) + '"><img alt="acces fiche historique" class="icon" src="../../../static/images/modifier.svg"/></a>'
        })
    problemes = Probleme.objects.all()
    problemes_table = []
    for item in problemes:
        # TODO : couleur pour le problème
        problemes_table.append({
            'C': '',
            'Date du sinistre': item.date_signalement,
            'Agence': item.id_agence.nom,
            'Agent': item.id_agent_ouverture.prenom + ' ' + item.id_agent_ouverture.nom,
            'Dernier message': item.probleme,
            'M': '<a href="' + str(item.id) + '"><img alt="acces fiche probleme" class="icon" src="../../../static/images/modifier.svg"/></a>'
        })
    if request.user.groups.filter(name="administrateur").exists():
        options = []
        agences = Agence.objects.all()
        for item in agences:
            options.append(item.nom)
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
            if request.POST.get('agence') and request.POST.get('agence') != vehicule.id_agence.nom:
                vehicule.id_agence = Agence.objects.get(nom=request.POST.get('agence'))
            vehicule.save()
            return render(request, '../templates/vehicule/ficheVehiculeAdmin.html',
                          {'confirmation': True,
                           'vehicule': vehicule,
                           'photos': photos,
                           'options': options,
                           'historiques_table': historiques_table,
                       'problemes_table': problemes_table})
        return render(request, '../templates/vehicule/ficheVehiculeAdmin.html',
                      {'vehicule': vehicule,
                       'photos': photos,
                       'options': options,
                       'historiques_table': historiques_table,
                       'problemes_table': problemes_table})
    else:
        return render(request, '../templates/vehicule/ficheVehiculeUser.html',
                      {'vehicule': vehicule,
                       'photos': photos,
                       'historiques_table': historiques_table,
                       'problemes_table': problemes_table})


@login_required()
def supprimer(request, id_vehicule):
    if request.user.groups.filter(name="administrateur").exists():
        vehicule = Vehicule.objects.get(id=id_vehicule)
        if request.method == 'POST':
            vehicule.delete()
            return redirect('vehicules')
        return render(request, '../templates/vehicule/confirmationSuppressionVehicule.html',
                      {'vehicule': vehicule})
