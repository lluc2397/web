# Generated by Django 3.1.2 on 2021-02-20 18:20

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('escuela', '0003_auto_20210219_2309'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cursos',
            name='alumnos',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='talleres',
            name='alumnos',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
