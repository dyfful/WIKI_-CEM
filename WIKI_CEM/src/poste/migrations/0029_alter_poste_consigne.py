# Generated by Django 4.0.1 on 2022-01-12 13:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0028_alter_poste_automatismeposte_alter_poste_cco_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poste',
            name='Consigne',
            field=models.ManyToManyField(blank=True, to='poste.Consigne'),
        ),
    ]
