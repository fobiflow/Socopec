from django.db import models
from vehicule.models import Photo

#  TODO : penser à ajouter une agence "générale" Socopec pour admin

class Agence(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE)
    nom = models.CharField(max_length=50)
    adresse = models.TextField()
    tel = models.CharField(max_length=15)
    fax = models.CharField(max_length=15)

    class Meta:
        verbose_name = "agence"
        ordering = ['id']

    def __str__(self):
        return self.id
