# Generated by Django 3.1.2 on 2021-02-28 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cartera', '0003_auto_20210226_1345'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cartera',
            name='observacion',
            field=models.CharField(blank=True, default='', max_length=500, null=True, verbose_name='Observaciones'),
        ),
        migrations.AlterField(
            model_name='cartera',
            name='rendimiento',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, max_digits=10, null=True, verbose_name='Rendimiento'),
        ),
    ]
