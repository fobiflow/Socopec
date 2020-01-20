from django.urls import include, path
from accueil import views

urlpatterns = [
    path('', views.connect, name='connect'),
    path('', include('django.contrib.auth.urls')),
    path('accueil', views.accueil, name='accueil'),
    path('password/', views.password, name='password'),
    path('logout/', views.disconnect, name='logout')
]