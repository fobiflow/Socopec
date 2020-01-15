from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import ConnexionForm


def connexion(request):
    error = False

    if request.method == "POST":
        form = ConnexionForm(request.POST)
        if form.is_valid():
            identifiant = form.cleaned_data["identifiant"]
            mot_de_passe = form.cleaned_data["mot_de_passe"]
            user = authenticate(identifiant=identifiant, mot_de_passe=mot_de_passe)
            if user:
                login(request, user)
            else:
                error = True
    else:
        form = ConnexionForm()

    return render(request, 'connexion/connexion.html', {'form': form})


def deconnexion(request):
    logout(request)
    return redirect(reverse(connexion))