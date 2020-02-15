from django.db import models


class Agence(models.Model):
    nom = models.CharField(max_length=30, default="à remplir")
    adresse = models.TextField(default="à remplis")
    complement_adresse = models.TextField(blank=True, null=True, default="null")
    code_postal = models.IntegerField(default=00000)
    ville = models.CharField(max_length=20, default="default_city")
    telephone = models.CharField(max_length=15, default="à remplir")
    fax = models.CharField(max_length=15, blank=True, null=True, default="null")
    photo = models.CharField(max_length=255, blank=True, null=True, default="null")

    class Meta:
        verbose_name = "agence"
        ordering = ['id']

    def __str__(self):
        return str(self.id)
