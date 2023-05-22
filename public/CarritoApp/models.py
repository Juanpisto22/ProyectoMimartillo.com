from django.db import models

# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=64)
    categoria = models.CharField(max_length=32)
    precio = models.IntegerField()

    def __str__(self):
        return f'{self.nombre} -> {self.precio}'
    
class Comentario(models.Model):
    autor = models.CharField(max_length=200)
    mensaje = models.TextField()
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.autor