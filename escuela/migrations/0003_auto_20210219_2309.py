# Generated by Django 3.1.2 on 2021-02-20 05:09

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('escuela', '0002_auto_20210219_2210'),
    ]

    operations = [
        migrations.AddField(
            model_name='cursos',
            name='alumnos',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='talleres',
            name='alumnos',
            field=models.ManyToManyField(blank=True, null=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='talleres',
            name='curso_relacionado',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='escuela.cursos'),
        ),
    ]