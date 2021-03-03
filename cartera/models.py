from django.db import models
from django.contrib.auth import get_user_model

MyUser = get_user_model()

Movimientos = [
   ( "COMPRA", "Compra"),
   ("VENTA", "Venta"),
]

class Activo (models.Model):
    nombre = models.CharField("Activo", max_length=250)

    def __str__(self):
        return self.nombre

class Cartera (models.Model):
    usuario = models.ForeignKey(MyUser,  on_delete=models.CASCADE, null=True, blank=True)
    activo = models.ForeignKey(Activo,  on_delete=models.PROTECT, null=True, blank=True)
    nombre_activo = models.CharField("Nombre del activo",max_length=250, null=True, blank=True)
    ticker_accion =models.CharField("Ticker",max_length=6, null=True, blank=True)
    rendimiento = models.DecimalField ("Rendimiento",null=True, blank=True, max_digits=10, decimal_places=2, default=0)
    valor = models.DecimalField ("Valor",null=True, blank=True, max_digits=100, decimal_places=2)
    cantidad = models.IntegerField("Cantidad", null=True, blank=True)
    movimiento = models.CharField("Movimiento realizado", choices=Movimientos, max_length=6, null=True, blank=True)
    fecha_movimiento = models.DateField("Fecha del movimiento", null=True, blank=True)
    observacion = models.CharField("Observaciones", max_length=500, null=True, blank=True, default="")

    def __str__(self):
        return '%s - %s - %s' % (self.usuario, self.activo, self.nombre_activo)
    
    def valor_total(self):
        return self.cantidad * self.valor

    