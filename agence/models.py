from django.db import models


class Agence(models.Model):
    nom = models.CharField(max_length=30)
    adresse = models.TextField()
    complement_adresse = models.TextField(blank=True, null=True)
    code_postal = models.IntegerField()
    ville = models.CharField(max_length=20)
    telephone = models.CharField(max_length=15)
    fax = models.CharField(max_length=15, blank=True, null=True)
    photo = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        verbose_name = "agence"
        ordering = ['id']

    def __str__(self):
        return self.id
