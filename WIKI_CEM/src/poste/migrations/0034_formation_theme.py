# Generated by Django 4.0.1 on 2022-01-19 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0033_typefiche_fiche'),
    ]

    operations = [
        migrations.CreateModel(
            name='Formation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Titre', models.CharField(max_length=40)),
                ('MaintenuPar', models.CharField(max_length=40)),
                ('Actualite', models.TextField()),
                ('PMC', models.TextField()),
                ('Fonctionnement', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Theme', models.CharField(max_length=40)),
                ('ModuleFormation', models.CharField(max_length=40)),
                ('QE', models.TextField()),
                ('Outils', models.TextField()),
                ('Divers', models.TextField()),
            ],
        ),
    ]
