from django.db import models

# Create your models here.
from django.db import models

class Producto(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=32)
    precio = models.IntegerField()
    cantidad = models.IntegerField(default=0)  # campo de la cantidad de productos
    descripcion = models.CharField(max_length=200, null=True)
    link_img = models.CharField(max_length=200, null=True)
    activo = models.BooleanField(default=True)  # Nuevo campo de activación

    def __str__(self):
        return f'ID: {self.id} - {self.nombre} -> {self.precio}'
    
class Comentario(models.Model):
    autor = models.CharField(max_length=200)
    mensaje = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.autor