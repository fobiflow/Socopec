from django.urls import path
from . import views

urlpatterns = [
    path('lister', views.lister, name='lister_agent'),
    path('creer', views.creer, name='creer_agent'),
    path('modifier/<id_agent>', views.modifier, name='modifier_agent'),
    path('supprimer/<id_agent>', views.supprimer, name='supprimer_agent'),
    path('voir/<id_agent>', views.voir, name='voir_agent')
]
