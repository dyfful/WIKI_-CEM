# Generated by Django 4.0.1 on 2022-03-16 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0003_commentaire'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fiche',
            name='Titre',
            field=models.CharField(max_length=60),
        ),
    ]