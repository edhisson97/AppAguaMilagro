# Generated by Django 4.1.5 on 2023-01-12 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clientes', '0004_alter_cifras_id_valores'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cifras',
            name='id_valores',
        ),
    ]
