from rest_framework import generics, status
from rest_framework.response import Response

from productoApp.models.producto import Producto
from productoApp.serializers.productoSerializer import ProductoSerializer

class ConsultaProductoIndividual(generics.RetrieveAPIView):

    def get_object(self, id):
        try:
            return Producto.objects.get(id=id)
        except Producto.DoesNotExist:
            return None

    def get(self, request, *args, **kwargs):
        producto = self.get_object(kwargs['pk'])
        if not producto:
            return Response(
            {"res": "Producto inexistente"},
            status=status.HTTP_400_BAD_REQUEST
            )
        serializer = ProductoSerializer(producto)
        return Response(serializer.data, status=status.HTTP_200_OK)