# Generated by Django 3.1.2 on 2020-11-15 09:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fftactics_api', '0005_auto_20201115_1726'),
    ]

    operations = [
        migrations.RenameField(
            model_name='job',
            old_name='class_name',
            new_name='Class_name',
        ),
    ]
