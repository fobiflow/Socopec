# Generated by Django 2.2.5 on 2020-01-26 20:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('historique', '0002_auto_20200126_2000'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historique',
            name='id_agence',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='agence.Agence'),
        ),
        migrations.AlterField(
            model_name='historique',
            name='id_agent',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='agent.Agent'),
        ),
        migrations.AlterField(
            model_name='historique',
            name='id_statut',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='historique.Statut'),
        ),
        migrations.AlterField(
            model_name='historique',
            name='id_vehicule',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vehicule.Vehicule'),
        ),
        migrations.AlterField(
            model_name='probleme',
            name='id_agent_ouverture',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='id_agent_ouverture', to='agent.Agent'),
        ),
        migrations.AlterField(
            model_name='probleme',
            name='id_agent_resolution',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='id_agent_resolution', to='agent.Agent'),
        ),
        migrations.AlterField(
            model_name='probleme',
            name='id_vehicule',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vehicule.Vehicule'),
        ),
    ]
