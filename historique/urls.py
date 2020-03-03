from django.urls import path
from . import views

urlpatterns = [
    path('vehicule/<id_vehicule>', views.creerHisto, name='new_historique'),
    # path('/<id_historique>', views.update, name="update_historique")
    # path('', views.generate, name='historique'),
]
