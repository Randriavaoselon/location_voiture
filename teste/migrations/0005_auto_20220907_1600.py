# Generated by Django 3.2.8 on 2022-09-07 13:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teste', '0004_department_employee'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='employee',
            name='deptid',
        ),
        migrations.DeleteModel(
            name='Form1',
        ),
        migrations.DeleteModel(
            name='Form2',
        ),
        migrations.DeleteModel(
            name='Form3',
        ),
        migrations.DeleteModel(
            name='department',
        ),
        migrations.DeleteModel(
            name='employee',
        ),
    ]
