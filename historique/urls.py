from django.urls import path
from . import views

urlpatterns = [
    path('lister', views.lister, name='lister_historique'),
    path('creer', views.creer, name='creer_historique'),
    path('modifier/<id_historique>', views.modifier, name='modifier_historique'),
    path('supprimer/<id_historique>', views.supprimer, name='supprimer_historique'),
    path('voir/<id_historique>', views.voir, name='voir_historique')
]
