from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate, name='agents'),
    path('supprimer/<id_agent>', views.supprimer, name='supprimer_agent'),
    path('<id_agent>', views.modifier, name='modifier_agent'),
]
