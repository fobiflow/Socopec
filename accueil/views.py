from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from agent.models import Agent


@login_required
def accueil(request):
    # TODO : ajout des éléments User
    identifiant = request.user.username
    agent = Agent.objects.get(identifiant=identifiant)
    if request.user.groups.filter(name="administrateur").exists():
        return render(request, '../templates/accueil/accueilAdmin.html', {'agent': agent})
    else:
        return render(request, '../templates/accueil/accueilUser.html', {'agent': agent})


def connect(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('accueil')
    else:
        error = False

        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("password")
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                return HttpResponseRedirect('accueil')
            else:
                error = True

        return render(request, 'accueil/login.html', locals())


def disconnect(request):
    logout(request)
    return HttpResponseRedirect('/')


def password(request):
    if request.method == "POST":
        mail = request.POST.get("email")
        return HttpResponseRedirect('/')

    return render(request, 'accueil/password.html', locals())
