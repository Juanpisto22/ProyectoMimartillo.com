from django.contrib import admin
from django.urls import path, include
from .views import *
from login.views import*


urlpatterns = [
    path('',tienda,name='Tienda'),
    path('agregar/<int:producto_id>/', agregar_producto, name="Add"),
    path('eliminar/<int:producto_id>/', eliminar_producto, name="Del"),
    path('restar/<int:producto_id>/', restar_producto, name="Sub"),
    path('limpiar/', limpiar_carrito, name="CLS"),
    path('buscar/', buscar_productos, name='buscar_productos'),
    path('comentarios/', comentarios , name='comentarios'),
    path('blogs/', manuales , name='manuales'),
]