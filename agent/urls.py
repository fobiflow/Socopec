from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate, name='agents'),
    path('/modifier/', views.mettre_a_jour, name='modifier_agents'),
]
