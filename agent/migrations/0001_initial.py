# Generated by Django 2.2.5 on 2019-10-02 07:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('agence', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=25)),
                ('prenom', models.CharField(max_length=25)),
                ('login', models.CharField(max_length=25)),
                ('mot_de_passe', models.CharField(max_length=50)),
                ('tel', models.CharField(max_length=15)),
                ('fax', models.CharField(max_length=15)),
                ('mobile', models.CharField(max_length=15)),
                ('id_agence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='agence.Agence')),
            ],
            options={
                'verbose_name': 'agent',
                'ordering': ['id'],
            },
        ),
    ]
