# Generated by Django 4.1.7 on 2023-05-30 01:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarritoApp', '0005_producto_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='link_img',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
