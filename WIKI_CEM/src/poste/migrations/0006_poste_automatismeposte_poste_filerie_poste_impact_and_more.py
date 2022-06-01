# Generated by Django 4.0.1 on 2022-01-09 18:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0005_automatismeposte_cco_filerie_impact_jdb_tension_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='poste',
            name='AutomatismePoste',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poste.automatismeposte'),
        ),
        migrations.AddField(
            model_name='poste',
            name='Filerie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poste.filerie'),
        ),
        migrations.AddField(
            model_name='poste',
            name='Impact',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poste.impact'),
        ),
        migrations.AddField(
            model_name='poste',
            name='JDB',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poste.jdb'),
        ),
        migrations.AddField(
            model_name='poste',
            name='Tension',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poste.tension'),
        ),
    ]