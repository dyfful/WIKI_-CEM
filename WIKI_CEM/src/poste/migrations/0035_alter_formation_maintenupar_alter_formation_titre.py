# Generated by Django 4.0.1 on 2022-01-19 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0034_formation_theme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formation',
            name='MaintenuPar',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='formation',
            name='Titre',
            field=models.CharField(max_length=100),
        ),
    ]
