# Generated by Django 4.1.5 on 2023-01-12 05:09

import clientes.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0003_valoresbase_cifras'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cifras',
            name='id_valores',
            field=models.IntegerField(null=True, verbose_name=clientes.models.ValoresBase),
        ),
    ]
