# Generated by Django 4.0.1 on 2022-03-29 13:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0062_alter_commentaire_statut'),
    ]

    operations = [
        migrations.CreateModel(
            name='TypePoste',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='poste',
            name='TypePoste',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poste.typeposte'),
        ),
    ]
