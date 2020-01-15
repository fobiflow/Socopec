from django.db import models
from agence.models import Agence
from vehicule.models import Vehicule
from agent.models import Agent
import datetime


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
    date_debut = models.DateTimeField(default=datetime.date.today)
    date_fin = models.DateTimeField(blank=True, null=True)
    localisation = models.CharField(max_length=50)

    class Meta:
        verbose_name = "historique"
        ordering = ['id']

    def __str__(self):
        return self.id


class Probleme(models.Model):
    id_vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE)
    id_agent_ouverture = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='id_agent_ouverture')
    id_agent_resolution = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='id_agent_resolution')
    probleme = models.TextField(blank=True, null=True)
    date_signalement = models.DateTimeField(default=datetime.date.today)
    date_resolution = models.DateTimeField(blank=True, null=True)

    class Meta:
        verbose_name = "probleme"
        ordering = ['id']

    def __str__(self):
        return self.id


