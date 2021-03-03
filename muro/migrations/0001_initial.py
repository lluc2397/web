# Generated by Django 3.1.2 on 2021-02-16 14:35

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Autores',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(blank=True, max_length=150, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Libros',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(blank=True, max_length=150, null=True)),
                ('fecha_edicion', models.CharField(blank=True, max_length=150, null=True)),
                ('img_portada', models.ImageField(blank=True, null=True, upload_to='libros/')),
                ('resumen', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('libro', models.FileField(blank=True, null=True, upload_to='libros/')),
                ('autor', models.ForeignKey(blank=True, max_length=150, null=True, on_delete=django.db.models.deletion.PROTECT, to='muro.autores')),
                ('genero', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='web.category')),
            ],
        ),
    ]
