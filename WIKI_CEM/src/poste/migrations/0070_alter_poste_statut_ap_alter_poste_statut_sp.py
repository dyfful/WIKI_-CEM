# Generated by Django 4.0.1 on 2022-04-12 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0069_poste_statut_ap_poste_statut_sp_alter_zone_poste'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poste',
            name='statut_ap',
            field=models.BooleanField(default=False, verbose_name='AUTRE PARTICULARITER ETAT'),
        ),
        migrations.AlterField(
            model_name='poste',
            name='statut_sp',
            field=models.BooleanField(default=False, verbose_name='SCHEMAS PREFERENTIEL ETAT'),
        ),
    ]