from django.urls import path
from agence import views

urlpatterns = [
    path('', views.generate, name='agences'),
    path('<id_agence>', views.fiche, name='fiche_agence')
]
