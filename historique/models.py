from django.db import models
from agence.models import Agence
from vehicule.models import Vehicule
from agent.models import Agent
import datetime


class Statut(models.Model):
    statut = models.CharField(max_length=20, default="àremplir")

    class Meta:
        verbose_name = "statut"
        ordering = ['id']

    def __str__(self):
        return self.id


class Historique(models.Model):
    id_agence = models.ForeignKey(Agence, on_delete=models.CASCADE, default=1)
    id_vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, default=1)
    id_statut = models.ForeignKey(Statut, on_delete=models.CASCADE, default=1)
    id_agent = models.ForeignKey(Agent, on_delete=models.CASCADE, default=1)
    date_debut = models.DateTimeField(default=datetime.date.today)
    date_fin = models.DateTimeField(blank=True, null=True, default="null")
    localisation = models.CharField(max_length=50, default="àremplir")

    class Meta:
        verbose_name = "historique"
        ordering = ['id']

    def __str__(self):
        return self.id


class Probleme(models.Model):
    id_vehicule = models.ForeignKey(Vehicule, on_delete=models.CASCADE, default=1)
    id_agent_ouverture = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='id_agent_ouverture', default=1)
    id_agent_resolution = models.ForeignKey(Agent, on_delete=models.CASCADE, related_name='id_agent_resolution', default=1)
    probleme = models.TextField(blank=True, null=True, default="null")
    date_signalement = models.DateTimeField(default=datetime.date.today)
    date_resolution = models.DateTimeField(blank=True, null=True, default="null")

    class Meta:
        verbose_name = "probleme"
        ordering = ['id']

    def __str__(self):
        return self.id


