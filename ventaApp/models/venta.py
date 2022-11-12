import imp
from django.db import models
from productoApp.models import Producto
from usuarioApp.models import User


class Venta(models.Model):
    usuario = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
    fecha_venta = models.DateField('FechaVenta')
    valor_total_venta = models.FloatField('ValorTotalVenta')
    venta_producto = models.ManyToManyField(Producto)