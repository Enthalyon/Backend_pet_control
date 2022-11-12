from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from productoApp.models.producto import Producto
from productoApp.serializers.productoSerializer import ProductoSerializer

class ProductCreateView(APIView):
    permission_classes = (IsAuthenticated,)

    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = ProductoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)