from django.urls import path
from connexion import views

urlpatterns = [
    path('', views.connexion, name='connexion'),
    path('/logout', views.deconnexion, name='deconnexion')
]