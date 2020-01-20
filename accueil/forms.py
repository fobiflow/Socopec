from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(label="Identifiant", max_length=30)
    password = forms.CharField(label="Mot de passe", widget=forms.PasswordInput)


class PasswordForm(forms.Form):
    email = forms.CharField(label="Adresse email ou pseudo", max_length=50)
