from django.urls import path
from . import views

urlpatterns = [
    path('lister', views.lister, name='lister_agence'),
    path('creer/', views.creer, name='creer_agence'),
    path('modifier/<id_agence>', views.modifier, name='modifier_agence'),
    path('supprimer/<id_agence>', views.supprimer, name='supprimer_agence'),
    path('voir/<id_agence>', views.voir, name='voir_agence')
]
