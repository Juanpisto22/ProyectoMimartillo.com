# Generated by Django 4.1.7 on 2023-05-26 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CarritoApp', '0003_alter_producto_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='cantidad',
            field=models.IntegerField(default=0),
        ),
    ]
