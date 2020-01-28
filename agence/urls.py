from django.urls import path
from agence import views

urlpatterns = [
    path('', views.generate, name='agences'),
]
