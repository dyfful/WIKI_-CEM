# Generated by Django 4.0.1 on 2022-01-09 21:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0013_po_zone_po'),
    ]

    operations = [
        migrations.CreateModel(
            name='ACR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelle', models.CharField(max_length=20)),
            ],
            options={
                'verbose_name': 'ACR',
                'ordering': ['libelle'],
            },
        ),
        migrations.AlterModelOptions(
            name='po',
            options={'ordering': ['libelle'], 'verbose_name': 'PO'},
        ),
        migrations.AddField(
            model_name='zone',
            name='ACR',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poste.acr'),
        ),
    ]
