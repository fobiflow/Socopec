from django.db import models
from agence.models import Agence
from vehicule.models import Vehicule
from agent.models import Agent


class Statut(models.Model):
    statut = models.CharField(max_length=20)

    class Meta:
        verbose_name = "statut"
        ordering = ['id']

    def __str__(self):
        return self.id


class Historique(models.Model):
    id_agence = models.ForeignKey(Agence, on_delete=models.CASCADE)
    id_vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    id_statut = models.ForeignKey(Statut, on_delete=models.CASCADE)
    id_agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    date_debut = models.DateTimeField()
    date_fin = models.DateTimeField()
    probleme = models.TextField()

    class Meta:
        verbose_name = "historique"
        ordering = ['id']

    def __str__(self):
        return self.id
