from django.urls import path
from . import views

urlpatterns = [
    path('lister', views.lister, name='lister_vehicule'),
    path('creer', views.creer, name='creer_vehicule'),
    path('modifier/<id_vehicule>', views.modifier, name='modifier_vehicule'),
    path('supprimer/<id_vehicule>', views.supprimer, name='supprimer_vehicule'),
    path('voir/<id_vehicule>', views.voir, name='voir_vehicule')
]
