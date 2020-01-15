from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import VehiculeForm
from .models import Vehicule

@login_required
def lister(request):
    vehicules = Vehicule.objects.all()
    return render(request, 'vehicule/lister.html', {'vehicules': vehicules})


def creer(request):
    if request.POST:
        form = VehiculeForm(request.POST)
        if form.is_valid:
            form.save()
            return redirect('lister_vehicule')
    else:
        form = VehiculeForm()
    return render(request, 'vehicule/creer.html', {'form': form})


def modifier(request, id_vehicule):
    vehicule = get_object_or_404(Vehicule, id=id_vehicule)
    form = VehiculeForm(request.POST or None, instance=vehicule)
    if form.is_valid():
        form.save()
        return redirect('lister_vehicule')
    return render(request, 'vehicule/modifier.html', {'form': form, 'id_vehicule': id_vehicule})


def supprimer(request, id_vehicule):
    vehicule = Vehicule.objects.get(id=id_vehicule)
    vehicule.delete()
    return render(request, 'vehicule/supprimer.html', locals())


def voir(request, id_vehicule):
    vehicule = Vehicule.objects.get(id=id_vehicule)
    return render(request, 'vehicule/voir.html', {'vehicule': vehicule})