from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from ventaApp.models.venta import Venta
from ventaApp.serializers.ventaSerializer import VentaSerializer

class ConsultaVentaView(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated]
    
    def get (self, request, *args, **kwargs):
        ventas = Venta.objects.all()
        serializer_class = VentaSerializer(ventas,many = True)
        return Response (serializer_class.data, status=status.HTTP_200_OK)

    
