from datetime import date, datetime

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
    for item in data:
        color = "white"
        if Probleme.objects.filter(id_vehicule=item, statut="en cours").exists():
            color = "orange"
        if Probleme.objects.filter(id_vehicule=item, statut="en cours",
                                   date_signalement=date.today().strftime('%Y-%m-%d 00:00:00.0000')).exists():
            color = "red"
        localisation = ""
        statut = ""
        dates = ""
        if Historique.objects.filter(id_vehicule=item, statut="en cours").exists():
            localisation = Historique.objects.get(id_vehicule=item, statut="en cours").localisation
            statut = Historique.objects.get(id_vehicule=item, statut="en cours").id_statut.statut
            if Historique.objects.get(id_vehicule=item, statut="en cours").date_fin:
                dates = Historique.objects.get(id_vehicule=item, statut="en cours").date_debut.strftime('%d/%m/%Y') + \
                        " au " + Historique.objects.get(id_vehicule=item, statut="en cours").date_fin.strftime(
                    '%d/%m/%Y')
            else:
                dates = Historique.objects.get(id_vehicule=item, statut="en cours").date_debut.strftime(
                    '%d/%m/%Y') + " au --/--/----"
        vehicules_table.append({
            'P': '<div style="margin-left:2px;width:12px;height:28px;background-color:' + color + '"></div>',
            'Plaque': item.immatriculation,
            'Agence': item.id_agence.nom,
            'Modèle': item.modele,
            'Statut': statut,
            'Localisation': localisation,
            'Dates': dates,
            'Date de fab.': item.date_fabrication.strftime('%d-%m-%Y'),
            'CV': item.puissance,
            'Poids': item.poids,
            'H': item.hauteur,
            'L': item.largeur,
            'o': '<a href="' + str(
                item.id) + '"><img alt="acces fiche vehicule" class="icon" src="../../../static/images/oeuil.svg"/></a>',
        })
    # Vue pour Admin :
    if request.user.groups.filter(name="administrateur").exists():
        actu = time.strftime('%A %d-%m-%Y')
        # Pour les stats :
        total_vehicules = data.count()
        statuts = []
        res = Statut.objects.all()
        boots = ["", "bg-success", "bg-warning", "bg-danger", "bg-info", "", "bg-success", "bg-warning", "bg-danger", ""]
        i = 0
        for item in res:
            value = Historique.objects.filter(id_statut=item.id, statut="en cours").count()
            pourcentage = int((value * 100) / total_vehicules)
            new = False
            if item.id > 5:
                new = True
            statuts.append({
                'id': item.id, 'statut': item.statut, 'value': value, "boots": boots[i], "pourcentage": pourcentage, 'new': new
            })
            i += 1
        problemes_orange = Probleme.objects.filter(statut="en cours").count()
        problemes_rouge = Probleme.objects.filter(
            date_signalement=datetime.today().strftime('%Y-%m-%d 00:00:00.00000')).count()
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
                already = False
                for item in data:
                    if item.immatriculation == request.POST.get('immatriculation'):
                        already = True
                if already == True:
                    return render(request, '../templates/vehicule/vehiculeAdmin.html',
                           {'already': True,
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
                    new_historique = Historique(
                        id_agence=Agence.objects.get(nom=request.POST.get('agence')),
                        id_vehicule=Vehicule.objects.get(immatriculation=request.POST.get('immatriculation')),
                        id_statut=Statut.objects.get(statut="En stationnement"),
                        id_agent=agent,
                        date_debut=date.today(),
                        statut="en cours",
                        localisation=Agence.objects.get(nom=request.POST.get('agence')).ville
                    )
                    new_historique.save()
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
    return render(request, '../templates/vehicule/vehiculeUser.html',
                  {'agent': agent, 'vehicules_table': vehicules_table})


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
    historique_en_cours = ''
    if Historique.objects.filter(id_vehicule=vehicule, statut="en cours").exists():
        historique_en_cours = Historique.objects.get(id_vehicule=vehicule, statut="en cours")
    for item in historiques:
        if item.date_debut and item.date_fin:
            dt = item.date_debut.strftime('%d/%m/%Y') + ' au ' + item.date_fin.strftime('%d/%m/%Y')
        else:
            dt = item.date_debut.strftime('%d/%m/%Y') + ' au --/--/--'
        historiques_table.append({
            'Dates': dt,
            'Statut': item.id_statut.statut,
            'Agence': item.id_agence.nom,
            'Agent': item.id_agent.prenom + ' ' + item.id_agent.nom,
            'Modifier': '<a href="historique/update/' + str(
                item.id) + '"><img alt="acces fiche historique" class="icon" src="../../../static/images/modifier.svg"/></a>'
        })
    problemes = Probleme.objects.filter(id_vehicule=vehicule)
    problemes_table = []
    for item in problemes:
        color = "white"
        if item.statut == "en cours":
            color = "orange"
        if item.date_signalement.strftime('%d/%m/%Y') == date.today().strftime('%d/%m/%Y'):
            color = "red"
        close = ''
        if item.statut == "en cours":
            close = '<a href="probleme/close/' + str(
                item.id) + '"><img alt="acces_fiche_fin_probleme" class="icon" src="../../../static/images/supprimer.svg"/></a>'
        problemes_table.append({
            'P': '<div style="margin-left:2px;height:28px;width:12px;background-color:' + color + '"></div>',
            'Date du sinistre': item.date_signalement.strftime('%d/%m/%Y'),
            'Agence': item.id_agence.nom,
            'Agent': item.id_agent_ouverture.prenom + ' ' + item.id_agent_ouverture.nom,
            'Dernier message': item.probleme,
            'Modifier': '<a href="probleme/update/' + str(
                item.id) + '"><img alt="acces fiche probleme" class="icon" src="../../../static/images/modifier.svg"/></a>',
            'Cloturer': close
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
                           'historique_en_cours': historique_en_cours,
                           'problemes_table': problemes_table})
        return render(request, '../templates/vehicule/ficheVehiculeAdmin.html',
                      {'vehicule': vehicule,
                       'photos': photos,
                       'options': options,
                       'historiques_table': historiques_table,
                       'historique_en_cours': historique_en_cours,
                       'problemes_table': problemes_table})
    else:
        return render(request, '../templates/vehicule/ficheVehiculeUser.html',
                      {'vehicule': vehicule,
                       'photos': photos,
                       'historiques_table': historiques_table,
                       'historique_en_cours': historique_en_cours,
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
