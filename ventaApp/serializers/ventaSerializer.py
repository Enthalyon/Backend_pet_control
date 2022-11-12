from rest_framework import serializers
from ventaApp.models.venta import Venta

class VentaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venta
        fields = ['usuario', 'fecha_venta', 'valor_total_venta', 'venta_producto']