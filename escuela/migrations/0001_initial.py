# Generated by Django 3.1.2 on 2021-02-20 02:55

import ckeditor.fields
from django.db import migrations, models



class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='generos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generos_temas', models.CharField(blank=True, max_length=150, null=True, verbose_name='Géneros de los temas')),
            ],
        ),
        migrations.CreateModel(
            name='talleres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=150, null=True)),
                ('resumen', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('herramienta', models.FileField(blank=True, null=True, upload_to='taller/')),
                ('contenido_taller', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('audio', models.FileField(blank=True, null=True, upload_to='taller/')),
                ('pdf_ejercicio', models.FileField(blank=True, null=True, upload_to='taller/')),
                ('pdf_correcion', models.FileField(blank=True, null=True, upload_to='taller/')),
                ('genero', models.ManyToManyField(blank=True, to='escuela.generos')),
            ],
        ),
        migrations.CreateModel(
            name='cursos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=150, null=True)),
                ('resumen', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('audio', models.FileField(blank=True, null=True, upload_to='curso/')),
                ('pdf_curso', models.FileField(blank=True, null=True, upload_to='curso/')),
                ('genero', models.ManyToManyField(blank=True, to='escuela.generos')),
            ],
        ),
    ]