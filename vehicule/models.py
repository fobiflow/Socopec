from django.db import models
from agence.models import Agence


class Vehicule(models.Model):
    immatriculation = models.CharField(max_length=9, default="àremplir")
    modele = models.CharField(max_length=20, default="àremplir")
    date_fabrication = models.DateField(default="àremplir")
    hauteur = models.FloatField(default="àremplir")
    largeur = models.FloatField(default="àremplir")
    poids = models.FloatField(default="àremplir")
    puissance = models.IntegerField(default="àremplir")
    id_agence = models.ForeignKey(Agence, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = "vehicule"
        ordering = ['id']

    def __str__(self):
        return self.id


class Photo(models.Model):
    url = models.CharField(max_length=255, default="àremplir")
    id_vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, default=1)

    class Meta:
        verbose_name = "photo"
        ordering = ['id']

    def __str__(self):
        return self.id

