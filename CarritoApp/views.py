from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from CarritoApp.Carrito import Carrito
from CarritoApp.models import Producto
from CarritoApp.models import Comentario
from .forms import ComentarioForm
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from io import BytesIO
from django.contrib import messages
import stripe
stripe.api_key = 'tu_clave_secreta_de_stripe'


def tienda(request):
    productos = Producto.objects.all()
    return render(request, "tienda.html", {'productos':productos})

def manuales(request):
    return render (request, 'blog.html')

def descripcion_productos(request, producto_id):
    producto = Producto.objects.get(id=producto_id)
    return render(request, 'descripcion_productos.html', {'producto': producto})



def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Producto.objects.get(id=producto_id)

    # Verificar si la cantidad en el carrito ya alcanzó el stock disponible
    if str(producto_id) in carrito.carrito and carrito.carrito[str(producto_id)]['cantidad'] >= producto.cantidad:
        messages.error(request, "No hay más de este producto en stock")
        return redirect("Tienda")

    carrito.agregar(producto)

    item_carrito = carrito.carrito[str(producto_id)]
    item_carrito['precio'] = producto.precio  # Agrega el precio al diccionario

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
    else:
        productos = Producto.objects.all()
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

def procesar_pago(request):
    # Obtener los productos del carrito del usuario
    carrito = request.session.get('carrito', {})
    carrito_items = carrito.values()

    # Realizar las operaciones de pago y actualización de la base de datos aquí

    # Ejemplo de actualización de la base de datos: restar la cantidad de productos comprados
    for item in carrito_items:
        producto = Producto.objects.get(id=item['producto_id'])
        producto.cantidad -= item['cantidad']
        producto.save()

    # Limpiar el carrito después de procesar el pago
    request.session['carrito'] = {}

    # Obtén el total del carrito
    total_carrito = sum(item['precio'] * item['cantidad'] for item in carrito_items)

    # Renderiza la plantilla "pago_exitoso.html" y pasa el total del carrito y el carrito como contexto
    return render(request, 'pago_exitoso.html', {'total_carrito': total_carrito, 'carrito': carrito_items})


def pago_exitoso(request):
    # Obtén el total del carrito
    total_carrito = 0
    carrito = request.session.get('carrito', {})
    for key, value in carrito.items():
        total_carrito += value['precio'] * value['cantidad']

    # Renderiza la plantilla "pago_exitoso.html" y pasa el total del carrito y el carrito completo como contexto
    return render(request, 'pago_exitoso.html', {'total_carrito': total_carrito, 'carrito': carrito})


def generar_pdf(carrito, total_carrito):
    buffer = BytesIO()
    p = canvas.Canvas(buffer)

    p.setFont('Helvetica', 12)
    p.drawString(50, 750, "Resumen de pago:")
    p.drawString(50, 700, f"Total del carrito: ${total_carrito}")

    y = 650
    for key, item in carrito.items():
        producto = item['nombre']
        precio = item['precio']
        cantidad = item['cantidad']
        subtotal = precio * cantidad
        p.drawString(50, y, f"Producto: {producto}")
        p.drawString(150, y, f"Precio unitario: ${precio}")
        p.drawString(300, y, f"Cantidad: {cantidad}")
        p.drawString(400, y, f"Subtotal: ${subtotal}")
        y -= 50

    p.showPage()
    p.save()

    pdf = buffer.getvalue()
    buffer.close()

    return pdf


def descargar_resumen_pdf(request):
    carrito = request.session.get('carrito', {})
    total_carrito = sum(item['precio'] * item['cantidad'] for item in carrito.values())

    pdf = generar_pdf(carrito, total_carrito)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="resumen.pdf"'
    response.write(pdf)

    return response
