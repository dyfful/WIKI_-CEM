# Generated by Django 4.0.1 on 2022-04-04 12:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0065_alter_poste_consigne'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poste',
            name='Zone',
            field=models.ManyToManyField(blank=True, to='poste.Zone'),
        ),
    ]