# Generated by Django 3.2.8 on 2022-07-21 19:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_profile_cin'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cin',
            field=models.CharField(default='', max_length=12, null=True),
        ),
    ]
