# Generated by Django 3.2.8 on 2022-08-26 20:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('voiture', '0009_alter_vehicule_numserie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicule',
            name='numSerie',
            field=models.IntegerField(default=0, null=True),
        ),
    ]
