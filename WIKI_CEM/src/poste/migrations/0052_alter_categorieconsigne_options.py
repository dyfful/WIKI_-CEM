# Generated by Django 4.0.1 on 2022-03-16 13:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0051_remove_zone_acr_zone_acr'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorieconsigne',
            options={'ordering': ['libelle'], 'verbose_name': 'Categorie F'},
        ),
    ]
