# Generated by Django 4.0.1 on 2022-02-21 08:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0047_alter_commentaire_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='commentaire',
            options={'ordering': ['-Date']},
        ),
    ]
