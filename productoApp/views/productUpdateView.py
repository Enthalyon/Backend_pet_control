from rest_framework import status, views
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from productoApp.models.producto import Producto
from productoApp.serializers.productoSerializer import ProductoSerializer

class ProductUpdateView(views.APIView):
    queryset = Producto()
    serializer_class = ProductoSerializer
    permission_classes = (IsAuthenticated,)
    def get_object(self, id):
        try:
            return Producto.objects.get(id=id)
        except Producto.DoesNotExist:
            return None

    def put(self, request, *args, **kwargs):
        product_instance = self.get_object(kwargs['pk'])
        if not product_instance:
            return Response(
                {"res": "No existe el producto con el id indicado."},
                status=status.HTTP_400_BAD_REQUEST
            )
    
        serializer = ProductoSerializer(instance = product_instance, data=request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)