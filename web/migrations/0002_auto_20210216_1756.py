# Generated by Django 3.1.2 on 2021-02-16 23:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentweb',
            name='content',
            field=models.CharField(max_length=300),
        ),
    ]
