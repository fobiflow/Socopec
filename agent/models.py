from django.db import models
from agence.models import Agence
import datetime


class Agent(models.Model):
    nom = models.CharField(max_length=30)
    prenom = models.CharField(max_length=30)
    adresse = models.TextField()
    complement_adresse = models.TextField(blank=True, null=True)
    code_postal = models.IntegerField()
    ville = models.CharField(max_length=20)
    tel = models.CharField(max_length=15)
    fax = models.CharField(max_length=15, blank=True, null=True)
    mobile = models.CharField(max_length=15, blank=True, null=True)
    email = models.CharField(max_length=50)
    date_entree_socopec = models.DateField(default=datetime.date.today)
    poste_socopec = models.CharField(max_length=30)
    admin = models.BooleanField(default=False)
    identifiant = models.CharField(max_length=20)
    mot_de_passe = models.CharField(max_length=20)
    photo = models.CharField(max_length=255, blank=True, null=True)
    id_agence = models.ForeignKey(Agence, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "agent"
        ordering = ['id']

    def __str__(self):
        return self.id
