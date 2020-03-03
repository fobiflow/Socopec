"""Socopec URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('accueil.urls')),
    path('accueil/', include('accueil.urls')),
    path('password/', include('accueil.urls')),
    path('disconnect', include('accueil.urls')),
    path('vehicule/', include('vehicule.urls')),
    path('vehicule/historique/', include('historique.urls')),
    path('agent/', include('agent.urls')),
    path('agence/', include('agence.urls')),
    path('historique/', include('historique.urls'))
]
