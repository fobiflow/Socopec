# Generated by Django 2.2.5 on 2020-01-31 19:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agence', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vehicule',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('immatriculation', models.CharField(default='àremplir', max_length=9)),
                ('modele', models.CharField(default='àremplir', max_length=20)),
                ('date_fabrication', models.DateField(default='àremplir')),
                ('hauteur', models.FloatField(default='àremplir')),
                ('largeur', models.FloatField(default='àremplir')),
                ('poids', models.FloatField(default='àremplir')),
                ('puissance', models.IntegerField(default='àremplir')),
                ('id_agence', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='agence.Agence')),
            ],
            options={
                'verbose_name': 'vehicule',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(default='àremplir', max_length=255)),
                ('id_vehicule', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='vehicule.Vehicule')),
            ],
            options={
                'verbose_name': 'photo',
                'ordering': ['id'],
            },
        ),
    ]
