# Generated by Django 3.2.8 on 2022-08-03 11:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paiement', '0004_auto_20220803_1318'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paiement',
            old_name='montants',
            new_name='total',
        ),
        migrations.AlterField(
            model_name='paiement',
            name='date_pay',
            field=models.DateTimeField(default=datetime.datetime(2022, 8, 3, 14, 22, 19, 113980)),
        ),
    ]