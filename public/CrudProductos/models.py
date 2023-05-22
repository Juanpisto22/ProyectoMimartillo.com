from django.db import models

# Create your models here.

class Item(models.Model):
    NombreP = models.CharField(max_length=100)
    DescripcionP = models.TextField()
