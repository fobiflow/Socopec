from django.urls import path
from . import views

urlpatterns = [
    path('', views.generate, name='agents'),
    path('supprimer/<id_agent>', views.supprimer, name='supprimer_agent'),
    path('modifier', views.modifier, name='modifier_agent'),
    path('modifierAdmin/<id_agent>', views.modifier_admin, name='modifier_agent_admin')
]
