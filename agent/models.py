from django.db import models
from agence.models import Agence


class Agent(models.Model):
    nom = models.CharField(max_length=25)
    prenom = models.CharField(max_length=25)
    login = models.CharField(max_length=25)
    mot_de_passe = models.CharField(max_length=50)
    tel = models.CharField(max_length=15)
    fax = models.CharField(max_length=15)
    mobile = models.CharField(max_length=15)
    admin = models.BooleanField(default=False)
    # id_agence = models.ForeignKey(Agence, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "agent"
        ordering = ['id']

    def __str__(self):
        return self.id
