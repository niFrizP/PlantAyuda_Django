# Generated by Django 4.0.4 on 2022-07-04 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_producto_imagen_producto_marca_producto_precio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='descripcion',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='producto',
            name='marca',
            field=models.CharField(max_length=80),
        ),
    ]