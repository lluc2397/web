# Generated by Django 3.1.2 on 2021-02-18 00:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0002_auto_20210216_1756'),
    ]

    operations = [
        migrations.RenameField(
            model_name='perfil',
            old_name='perfuser',
            new_name='user',
        ),
    ]
