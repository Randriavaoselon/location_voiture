# Generated by Django 3.2.8 on 2022-07-30 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('agence', '0005_alter_agence_useragence'),
        ('location', '0009_alter_location_userloueur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='userLoueur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user_loueur', to='agence.agence'),
        ),
    ]
