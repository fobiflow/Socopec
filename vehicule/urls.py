from django.urls import path
from vehicule import views

urlpatterns = [
    path('', views.generate, name='vehicules'),
    path('<id_vehicule>', views.fiche, name='fiche_vehicule'),
    path('supprimer/<id_vehicule>', views.supprimer, name='supprimer_vehicule')
]
