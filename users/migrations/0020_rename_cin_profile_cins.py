# Generated by Django 3.2.8 on 2022-08-17 05:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_profile_cin'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='cin',
            new_name='cins',
        ),
    ]
