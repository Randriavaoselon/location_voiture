# Generated by Django 3.2.8 on 2022-08-26 19:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paiement', '0020_alter_paiement_date_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paiement',
            name='date_pay',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 26, 22, 9, 42, 568528)),
        ),
    ]
