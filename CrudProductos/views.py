
from django.http.response import HttpResponse
from django.shortcuts import render, redirect 
from .models import*
from django.contrib import messages
from CarritoApp.Carrito import Carrito
from CarritoApp.models import *
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django_filters.views import FilterView
from .filters import ProductoFilter




# Create your views here.

def CrudProductos(request):
    return render (request, 'CrudProductos.html')




''' Views para los productos de la App CarritoApp '''

def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'listar_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        nombre = request.POST['nombre']
        categoria = request.POST['categoria']
        precio = request.POST['precio']
        cantidad = request.POST['cantidad']  # Nueva línea para obtener la cantidad
        descripcion = request.POST['descripcion']
        link_img = request.POST['link_img']
        Producto.objects.create(nombre=nombre, categoria=categoria, precio=precio, cantidad=cantidad, descripcion=descripcion,link_img=link_img)
        return redirect('listar_productos')
    return render(request, 'agregar_producto.html')

def editar_producto(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    if request.method == 'POST':
        if 'nombre' in request.POST and 'categoria' in request.POST:
            producto.nombre = request.POST['nombre']
            producto.categoria = request.POST['categoria']
            producto.precio = request.POST['precio']
            cantidad = request.POST.get('cantidad', 0)
            producto.descripcion = request.POST['descripcion']
            producto.link_img = request.POST['link_img']
            producto.cantidad = int(cantidad)
            producto.save()
            return redirect('listar_productos')
        else:
            # Manejar el caso cuando los campos obligatorios no están presentes en la solicitud POST
            return HttpResponse("Error: Los campos obligatorios no están completos.")
    return render(request, 'editar_producto.html', {'producto': producto})


@csrf_exempt
def toggle_producto(request):
    if request.method == 'POST':
        producto_id = request.POST.get('producto_id')
        activo = request.POST.get('activo')
        producto = Producto.objects.get(id=producto_id)
        producto.activo = activo == 'true'
        producto.save()
        return JsonResponse({'status': 'OK'})
    return JsonResponse({'status': 'ERROR', 'message': 'Invalid request method.'})

#Para buscar y filtrar productos
def buscar_productosc(request):
    query = request.GET.get('q')
    categoria_actual = request.GET.get('categoria')
    productos = None
    categorias = Producto.objects.values_list('categoria', flat=True).distinct()  # esta es la línea que debes actualizar
    if query and categoria_actual:
        productos = Producto.objects.filter(nombre__icontains=query, categoria__iexact=categoria_actual)
    elif query:
        productos = Producto.objects.filter(nombre__icontains=query)
    elif categoria_actual:
        productos = Producto.objects.filter(categoria__iexact=categoria_actual)
    else:
        productos = Producto.objects.all()  # Obtener todos los productos sin aplicar ningún filtro
    return render(request, 'listar_productos.html', {'productos': productos, 'query': query, 'categoria_actual': categoria_actual, 'categorias': categorias})