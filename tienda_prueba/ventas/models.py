from datetime import datetime
from django.db import models

from usuarios.models import Usuario

# Create your models here.


class Producto(models.Model):
    tipo = models.CharField(max_length=50)
    nombre = models.CharField(max_length=250)
    precio = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"{self.nombre}"


class Venta(models.Model):
    cliente = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=7, decimal_places=2)
    forma_pago = models.DecimalField(
        max_digits=7, decimal_places=2, verbose_name="Forma de pago"
    )
    vuelto = models.DecimalField(max_digits=7, decimal_places=2)
    fecha_recepcion = models.DateTimeField(
        auto_now_add=True, verbose_name="Fecha de recepción"
    )
    fecha_entrega = models.DateTimeField(verbose_name="Fecha de entrega")
    productos = models.ManyToManyField(Producto, through="DetalleVenta")

    def __str__(self):
        fecha_texto = datetime.strftime(self.fecha_recepcion, "%Y-%m-%d %H:%M")
        return f"{self.cliente} - {fecha_texto}"


class DetalleVenta(models.Model):
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.DecimalField(max_digits=7, decimal_places=3)
