# Generated by Django 3.1.2 on 2021-02-26 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perfil', '0004_follow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='perfil',
            name='ip_adresse',
        ),
        migrations.AlterField(
            model_name='perfil',
            name='facebook',
            field=models.CharField(blank=True, max_length=3000, null=True, verbose_name='Link de tú Facebook'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='instagram',
            field=models.CharField(blank=True, max_length=3000, null=True, verbose_name='Link de tú Instagram'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='pinterest',
            field=models.CharField(blank=True, max_length=3000, null=True, verbose_name='Link de tú Pinterest'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='tiktok',
            field=models.CharField(blank=True, max_length=3000, null=True, verbose_name='Link de tú Tiktok'),
        ),
        migrations.AlterField(
            model_name='perfil',
            name='twitter',
            field=models.CharField(blank=True, max_length=3000, null=True, verbose_name='Link de tú Twitter'),
        ),
    ]