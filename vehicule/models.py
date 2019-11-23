from django.db import models


class Vehicule(models.Model):
    immatriculation = models.CharField(max_length=9)
    modele = models.CharField(max_length=25)
    date_fabrication = models.DateField()
    hauteur = models.FloatField()
    largeur = models.FloatField()
    poids = models.FloatField()
    puissance = models.IntegerField()

    class Meta:
        verbose_name = "vehicule"
        ordering = ['id']

    def __str__(self):
        return self.id


class Photo(models.Model):
    url = models.CharField(max_length=255)
    id_vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "photo"
        ordering = ['id']

    def __str__(self):
        return self.id

