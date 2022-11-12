from rest_framework import serializers
from productoApp.models.producto import Producto

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'url_imagen', 'nombre', 'cantidad', 'descripcion', 'precio']