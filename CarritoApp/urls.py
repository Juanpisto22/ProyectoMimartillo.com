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
    path('descripcion_productos<int:producto_id>/',descripcion_productos, name='descripcion_productos'),
    path('blogs/', manuales , name='manuales'),
    path('procesar_pago/', procesar_pago, name='procesar_pago'),
    path('pago_exitoso/', pago_exitoso, name='pago_exitoso'),
    path('descargar_resumen_pdf/',descargar_resumen_pdf, name='descargar_resumen_pdf'),

]