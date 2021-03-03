# Generated by Django 3.1.6 on 2021-02-18 23:18

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('usuario', '0005_auto_20210216_1756'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='telefono',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, null=True, region=None, verbose_name='Número telefónico'),
        ),
    ]