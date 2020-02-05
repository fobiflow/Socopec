from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate, name='agents'),
    path('/modifier/', views.modifier_agents, name='modifier_agents'),
]
