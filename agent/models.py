from django.db import models
from agence.models import Agence
import datetime


class Agent(models.Model):
    nom = models.CharField(max_length=30, default="àremplir")
    prenom = models.CharField(max_length=30, default="àremplir")
    sexe = models.CharField(max_length=1)
    adresse = models.TextField(default="àremplir")
    complement_adresse = models.TextField(blank=True, null=True, default="null")
    code_postal = models.IntegerField(default=00000)
    ville = models.CharField(max_length=20, default="àremplir")
    tel = models.CharField(max_length=15, default="àremplir")
    fax = models.CharField(max_length=15, blank=True, null=True, default="null")
    mobile = models.CharField(max_length=15, blank=True, null=True, default="null")
    email = models.CharField(max_length=50, default="àremplir")
    date_entree_socopec = models.DateField(default=datetime.date.today)
    poste_socopec = models.CharField(max_length=30, default="àremplir")
    admin = models.BooleanField(default=False)
    identifiant = models.CharField(max_length=20, default="àremplir")
    mot_de_passe = models.CharField(max_length=20, default="àremplir")
    photo = models.CharField(max_length=255, blank=True, null=True, default="null")
    id_agence = models.ForeignKey(Agence, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "agent"
        ordering = ['id']

    def __str__(self):
        return str(self.id)
