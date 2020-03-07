from django.urls import path
from . import views

urlpatterns = [
    path('vehicule/<id_vehicule>', views.creerProbleme, name='new_probleme'),
    path('update/<id_probleme>', views.updateProbleme, name='update_probleme'),
    path('close/<id_probleme>', views.closeProbleme, name='close_probleme')
    # path('/<id_historique>', views.update, name="update_historique")
    # path('', views.generate, name='historique'),
]
