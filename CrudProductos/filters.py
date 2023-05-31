import django_filters
from CarritoApp.models import Producto

class ProductoFilter(django_filters.FilterSet):
    class Meta:
        model = Producto
        fields = {
            'nombre': ['icontains'],  # Filtrar por el campo 'nombre' usando una coincidencia parcial (icontains)
            'categoria': ['exact'],  # Filtrar por el campo 'categoria' exactamente
        }

