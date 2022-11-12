from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from productoApp.models.producto import Producto
from productoApp.serializers.productoSerializer import ProductoSerializer

class productDeleteView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]

    def get_object(self, id):
        try:
            return Producto.objects.get(id=id)
        except Producto.DoesNotExist:
            return None

    def delete(self, request, *args, **kwargs):
        branch_instance = self.get_object(kwargs['pk'])
        if not branch_instance:
            return Response(
                {"res":"El producto con el id ingresado no existe"},
                status=status.HTTP_400_BAD_REQUEST
            )
        branch_instance.delete()
        return Response(
            {"res":"Producto eliminado con exito!"},
            status=status.HTTP_200_OK
        )