# Generated by Django 4.0.1 on 2022-01-10 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poste', '0022_alter_typeclient_libelle'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='GMR',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='poste.gmr'),
        ),
    ]