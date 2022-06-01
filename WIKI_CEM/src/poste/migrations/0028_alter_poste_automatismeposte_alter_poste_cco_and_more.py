# Generated by Django 4.0.1 on 2022-01-12 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0027_alter_poste_protectionbarre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poste',
            name='AutomatismePoste',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='poste.automatismeposte'),
        ),
        migrations.AlterField(
            model_name='poste',
            name='CCO',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='poste.cco'),
        ),
        migrations.AlterField(
            model_name='poste',
            name='Filerie',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='poste.filerie'),
        ),
        migrations.AlterField(
            model_name='poste',
            name='JDB',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='poste.jdb'),
        ),
    ]