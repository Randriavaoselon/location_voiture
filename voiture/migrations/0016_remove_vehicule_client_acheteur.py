# Generated by Django 3.2.8 on 2022-09-25 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('voiture', '0015_vehicule_client_acheteur'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vehicule',
            name='client_acheteur',
        ),
    ]
