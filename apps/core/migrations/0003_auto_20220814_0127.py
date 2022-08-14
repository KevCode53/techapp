# Generated by Django 3.2 on 2022-08-14 01:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_department_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='code',
            field=models.CharField(max_length=5, unique=True, verbose_name='Código'),
        ),
        migrations.AlterField(
            model_name='department',
            name='name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Nombre'),
        ),
    ]
