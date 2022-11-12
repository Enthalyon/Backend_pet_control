from rest_framework.response import Response
from rest_framework.views import APIView

from productoApp.models.producto import Producto
from productoApp.serializers.productoSerializer import ProductoSerializer

class ConsultaProductoView(APIView):

    def get(self, request):
        productos = Producto.objects.all()
        productos_serializer = ProductoSerializer(productos,many = True)
        return Response (productos_serializer.data)