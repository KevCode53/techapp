# Generated by Django 3.2 on 2022-08-14 01:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ubications', '0002_alter_ubication_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Compromise',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.BooleanField(default=True, verbose_name='Estado')),
                ('created_date', models.DateField(auto_now_add=True, verbose_name='Fecha de Creación')),
                ('modified_date', models.DateField(auto_now=True, verbose_name='Fecha de Modificación')),
                ('deleted_date', models.DateField(auto_now=True, verbose_name='Fecha de Eliminacion')),
                ('year', models.SmallIntegerField(verbose_name='Año')),
                ('estimated_computers', models.PositiveSmallIntegerField(default=0, verbose_name='Computadoras Estimadas')),
                ('total_computers', models.PositiveSmallIntegerField(default=0, verbose_name='Computadoras Totales')),
                ('ubications', models.ManyToManyField(to='ubications.Ubication', verbose_name='Fiscalias')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Usuario')),
            ],
            options={
                'verbose_name': 'Compromiso',
                'verbose_name_plural': 'Compromisos',
                'unique_together': {('user', 'year')},
            },
        ),
    ]
