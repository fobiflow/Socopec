from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import LoginForm, PasswordForm
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required


@login_required
def accueil(request):
    if request.user.groups.filter(name="administrateur").exists():
        return render(request, 'accueil/accueilAdmin.html')
    else:
        return render(request, 'accueil/accueilUser.html')


def connect(request):
    error = False

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('accueil')
            else:
                error = True
    else:
        form = LoginForm()

    return render(request, 'accueil/login.html', locals())


def disconnect(request):
    logout(request)
    return HttpResponseRedirect('/')


def password(request):
    if request.method == "POST":
        form = PasswordForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/')
    else:
        form = PasswordForm()

    return render(request, 'accueil/password.html', locals())
