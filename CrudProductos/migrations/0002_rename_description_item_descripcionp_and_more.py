# Generated by Django 4.1.7 on 2023-03-13 04:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('CrudProductos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='item',
            old_name='description',
            new_name='DescripcionP',
        ),
        migrations.RenameField(
            model_name='item',
            old_name='name',
            new_name='NombreP',
        ),
    ]
