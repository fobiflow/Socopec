from django.urls import path
from agence import views

urlpatterns = [
    path('', views.generate, name='agences'),
    path('<id_agence>', views.fiche, name='fiche_agence'),
    path('supprimer/<id_agence>', views.supprimer, name='supprimer_agence'),
    # path('modifier/<id_agence>', views.modifier, name='modifier_agence')
]
