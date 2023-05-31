from django.contrib import admin
from django.urls import path
from CrudProductos.views import *


urlpatterns = [
    path('CrudProductos/', listar_productos, name='CrudProductos'),
    path('listar/', listar_productos, name='listar_productos'),
    path('agregar/', agregar_producto, name='agregar_producto'),
    path('editar/<int:producto_id>/', editar_producto, name='editar_producto'),
    path('toggle-producto/', toggle_producto, name='toggle_producto'),
    path('buscarCrud/', buscar_productosc, name='buscar_productosc'),
]
