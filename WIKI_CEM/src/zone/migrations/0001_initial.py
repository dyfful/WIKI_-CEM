# Generated by Django 4.0.1 on 2022-03-08 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('poste', '0050_alter_zone_gmr_alter_zone_groupement'),
    ]

    operations = [
        migrations.CreateModel(
            name='ACR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'ACR',
                'ordering': ['libelle'],
            },
        ),
        migrations.CreateModel(
            name='CategorieZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'Categorie Zone',
                'ordering': ['libelle'],
            },
        ),
        migrations.CreateModel(
            name='PO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=5)),
            ],
            options={
                'verbose_name': 'PO',
                'ordering': ['libelle'],
            },
        ),
        migrations.CreateModel(
            name='Zone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=20)),
                ('presentation', models.TextField(blank=True)),
                ('image', models.ImageField(blank=True, upload_to='zone')),
                ('ACR', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='zone.acr')),
                ('CategorieZone', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='zone.categoriezone')),
                ('GMR', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poste.gmr')),
                ('Groupement', models.ManyToManyField(to='poste.Groupement')),
                ('PO', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='zone.po')),
            ],
            options={
                'verbose_name': 'Zone',
                'ordering': ['libelle'],
            },
        ),
        migrations.CreateModel(
            name='Commentaire',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nom', models.CharField(max_length=50, verbose_name='Nom')),
                ('Prenom', models.CharField(max_length=50, verbose_name='Prénom')),
                ('Date', models.DateTimeField(auto_now=True)),
                ('Titre', models.CharField(max_length=30)),
                ('Contenu', models.TextField()),
                ('Zone', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='zone.zone', verbose_name='ZONE')),
            ],
            options={
                'ordering': ['-Date'],
            },
        ),
    ]
