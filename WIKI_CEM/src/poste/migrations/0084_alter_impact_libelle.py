# Generated by Django 4.0.1 on 2022-04-20 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0083_alter_filerie_libelle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='impact',
            name='libelle',
            field=models.CharField(max_length=20),
        ),
    ]
