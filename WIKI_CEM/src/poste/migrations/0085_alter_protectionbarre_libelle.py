# Generated by Django 4.0.1 on 2022-04-20 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0084_alter_impact_libelle'),
    ]

    operations = [
        migrations.AlterField(
            model_name='protectionbarre',
            name='libelle',
            field=models.CharField(max_length=5),
        ),
    ]
