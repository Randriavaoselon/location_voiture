# Generated by Django 3.2.8 on 2022-09-21 08:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_rename_cin_profile_cins'),
        ('voiture', '0014_auto_20220914_2030'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicule',
            name='client_acheteur',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='usr_acheteur', to='users.profile'),
        ),
    ]
