# Generated by Django 4.0.1 on 2022-01-12 13:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0031_alter_poste_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='poste',
            options={'ordering': ['libelle'], 'verbose_name': 'POSTE ÉLECTRIQUE', 'verbose_name_plural': 'POSTE ÉLECTRIQUES'},
        ),
    ]
