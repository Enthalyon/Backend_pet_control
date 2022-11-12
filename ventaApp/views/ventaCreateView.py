from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
 
from ventaApp.models.venta import Venta
from ventaApp.serializers.ventaSerializer import VentaSerializer
 
class VentaCreateView(APIView):
    permission_classes = (IsAuthenticated,)
   
    queryset = Venta.objects.all()
    serializer_class = VentaSerializer

    
    def post(self, request, *args, **kwargs):
        serializer = VentaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
                       
        return Response(serializer.data, status=status.HTTP_201_CREATED)