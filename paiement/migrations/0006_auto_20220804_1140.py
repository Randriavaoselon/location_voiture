# Generated by Django 3.2.8 on 2022-08-04 08:40

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('location', '0016_rename_userloueur_location_loueur'),
        ('paiement', '0005_auto_20220803_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paiement',
            name='date_pay',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 4, 11, 40, 58, 626547)),
        ),
        migrations.AlterField(
            model_name='paiement',
            name='id_loc',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='id_loc', to='location.location'),
        ),
    ]
