# Generated by Django 4.1.6 on 2023-05-02 21:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paiement', '0098_alter_paiement_date_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paiement',
            name='date_pay',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 3, 0, 44, 34, 142838)),
        ),
    ]