from django import forms
from .models import Agent
from django.forms import modelform_factory
from .models import Agence


class AgentForm(forms.Form):
    nom = forms.CharField(max_length=25)
    prenom = forms.CharField(max_length=25)
    login = forms.CharField(max_length=25)
    mot_de_passe = forms.CharField(max_length=50)
    tel = forms.CharField(max_length=15)
    fax = forms.CharField(max_length=15)
    mobile = forms.CharField(max_length=15)
    admin = forms.BooleanField()
    # agence = modelform_factory(Agence, fields=("nom",))
