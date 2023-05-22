from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from CarritoApp.Carrito import Carrito
from CarritoApp.models import Producto
from CarritoApp.models import Comentario
from .forms import ComentarioForm



def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos':productos})

def manuales(request):
    return render (request, 'blog.html')

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("Tienda")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("Tienda")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("Tienda")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("Tienda")

def buscar_productos(request):
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
    return render(request, 'tienda.html', {'productos': productos, 'query': query, 'categoria_actual': categoria_actual, 'categorias': categorias})


def comentarios(request):
    comentarios = Comentario.objects.order_by('-fecha_publicacion')
    if request.method == 'POST':
        form = ComentarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comentarios')
    else:
        form = ComentarioForm()
    return render(request, 'comentarios.html', {'comentarios': comentarios, 'form': form})

