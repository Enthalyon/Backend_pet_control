from django.db import models

class Producto(models.Model):
    url_imagen = models.CharField('UrlImagen', max_length=500)
    nombre = models.CharField('Nombre', max_length=50)
    cantidad = models.FloatField('Cantidad')
    descripcion = models.CharField('Descripcion', max_length=2000, default='Sin descripcion')
    precio = models.FloatField('Precio')