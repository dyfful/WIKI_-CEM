# Generated by Django 4.0.1 on 2022-05-03 14:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('theme', '0006_alter_fiche_image'),
        ('poste', '0100_commentaire_zone'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaire',
            name='Fiche',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='theme.fiche', verbose_name='FICHE'),
        ),
    ]
