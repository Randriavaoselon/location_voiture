# Generated by Django 4.1.6 on 2023-05-02 20:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('paiement', '0096_alter_paiement_date_pay'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paiement',
            name='date_pay',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 2, 23, 59, 37, 945457)),
        ),
    ]