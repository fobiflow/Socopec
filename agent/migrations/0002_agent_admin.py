# Generated by Django 2.2.5 on 2019-10-02 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agent', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agent',
            name='admin',
            field=models.BooleanField(default=False),
        ),
    ]
