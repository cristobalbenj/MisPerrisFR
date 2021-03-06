# Generated by Django 2.1.2 on 2018-11-06 08:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ciudad',
            options={'verbose_name': 'Ciudad', 'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='generoadoptante',
            options={'verbose_name': 'GeneroAdoptante', 'verbose_name_plural': 'GenerosAdoptantes'},
        ),
        migrations.AlterModelOptions(
            name='region',
            options={'verbose_name': 'Region', 'verbose_name_plural': 'Regiones'},
        ),
        migrations.AddField(
            model_name='adoptante',
            name='mascota',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.Mascota'),
        ),
        migrations.AddField(
            model_name='adoptante',
            name='vivienda',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.tipoVivienda'),
        ),
        migrations.AlterField(
            model_name='adoptante',
            name='tel',
            field=models.IntegerField(),
        ),
    ]
