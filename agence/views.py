from django.shortcuts import render, redirect, get_object_or_404
from .forms import AgenceForm
from .models import Agence


def generate(request):
    return render(request, '../templates/agences.html')


# def lister(request):
#     agences = Agence.objects.all()
#     return render(request, 'agence/lister.html', {'agences': agences})
#
#
# def creer(request):
#     if request.POST:
#         form = AgenceForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('lister_agence')
#     else:
#         form = AgenceForm()
#     return render(request, 'agence/creer.html', {'form': form})
#
#
# def modifier(request, id_agence):
#     agence = get_object_or_404(Agence, id=id_agence)
#     form = AgenceForm(request.POST or None, instance=agence)
#     if form.is_valid():
#         form.save()
#         return redirect('lister_agence')
#
#     return render(request, 'agence/modifier.html', {'form': form, 'id_agence': id_agence})
#
#
# def supprimer(request, id_agence):
#     agence = Agence.objects.get(id=id_agence)
#     agence.delete()
#     return render(request, 'agence/supprimer.html', locals())
#
#
# def voir(request, id_agence):
#     agence = Agence.objects.get(id=id_agence)
#     return render(request, 'agence/voir.html', {'agence': agence})
