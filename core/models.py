from django.db import models
from django.db.models.deletion import CASCADE
from django.forms import CharField

# Create your models here.


class Categoria(models.Model):
    nombre = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    nombre = models.CharField(max_length=80)
    stock = models.IntegerField()
    cod_producto = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=CASCADE)
    descripcion = models.CharField(max_length=80)

    def __str__(self):
        return self.nombre

