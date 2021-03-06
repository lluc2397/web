# Generated by Django 3.1.2 on 2021-02-23 06:09

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('escuela', '0008_auto_20210221_1946'),
    ]

    operations = [
        migrations.AddField(
            model_name='modulo',
            name='fecha_actualización',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Fecha actualización'),
        ),
        migrations.AddField(
            model_name='modulo',
            name='fecha_publicacion',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
