# Generated by Django 4.0.1 on 2022-03-08 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0049_delete_fiche_delete_typefiche'),
    ]

    operations = [
        migrations.AlterField(
            model_name='zone',
            name='GMR',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='GMR_Zone', to='poste.gmr'),
        ),
        migrations.AlterField(
            model_name='zone',
            name='Groupement',
            field=models.ManyToManyField(related_name='Groupement_Zone', to='poste.Groupement'),
        ),
    ]
