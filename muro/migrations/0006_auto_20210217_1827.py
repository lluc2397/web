# Generated by Django 3.1.2 on 2021-02-18 00:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('muro', '0005_auto_20210217_1324'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pedido',
            name='curs',
        ),
        migrations.RemoveField(
            model_name='pedido',
            name='tall',
        ),
        migrations.AddField(
            model_name='order',
            name='cantidad',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.DecimalField(blank=True, decimal_places=3, max_digits=10, null=True),
        ),
    ]
