# Generated by Django 4.0.1 on 2022-05-03 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0006_alter_fiche_image'),
        ('poste', '0102_commentairehistorique_zone'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commentaire',
            name='Fiche',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='theme.fiche', verbose_name='FICHE'),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='Poste',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='poste.poste', verbose_name='POSTE'),
        ),
        migrations.AlterField(
            model_name='commentaire',
            name='Zone',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='ZONE', to='poste.zone'),
        ),
    ]
