# Generated by Django 3.1.2 on 2021-02-28 05:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartera', '0004_auto_20210227_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartera',
            name='ticker_accion',
            field=models.CharField(blank=True, max_length=6, null=True, verbose_name='Ticker'),
        ),
    ]
