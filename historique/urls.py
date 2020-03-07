from django.urls import path
from . import views

urlpatterns = [
    path('statut', views.creerStatut, name='new_statut'),
    path('updateStatut/<id_statut>', views.updateStatut, name='update_statut'),
    path('deleteStatut/<id_statut>', views.deleteStatut, name='delete_statut'),
    path('vehicule/<id_vehicule>', views.creerHisto, name='new_historique'),
    path('update/<id_historique>', views.updateHisto, name='update_historique')
    # path('/<id_historique>', views.update, name="update_historique")
    # path('', views.generate, name='historique'),
]
