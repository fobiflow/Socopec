from django import forms


class ConnexionForm(forms.Form):
    identifiant = forms.CharField(label="Identifiant", max_length=30)
    mot_de_passe = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)