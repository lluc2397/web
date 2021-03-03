from django.db import models
from datetime import date, datetime
from django.urls import reverse
from ckeditor.fields import RichTextField
from django.utils import timezone
from web.models import Category
from django.contrib.auth import get_user_model

MyUser = get_user_model()

class Autores(models.Model):
    nombre = models.CharField(max_length=150,null=True, blank=True)

    def __str__(self):
        return self.nombre

class Libros(models.Model):
    titulo = models.CharField(max_length=150,null=True, blank=True)
    autor = models.ForeignKey(Autores, max_length=150,null=True, blank=True, on_delete= models.PROTECT)
    fecha_edicion = models.CharField(max_length=150, null=True, blank=True)
    img_portada = models.ImageField(upload_to='libros/',null=True, blank=True)
    resumen = RichTextField(null=True, blank=True)
    genero = models.ForeignKey(Category,  blank=True,  on_delete= models.PROTECT)
    libro = models.FileField(upload_to='libros/',null=True, blank=True)

    def __str__(self):
        return self.titulo

class servicios(models.Model):
    servicio = models.CharField("Nombre del servicio",max_length=150, null=True, blank=True)
    precio = models.DecimalField (null=True, blank=True, max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.servicio)

class productos(models.Model):
    producto = models.CharField("Nombre del producto", max_length=150, null=True, blank=True)
    precio = models.DecimalField (null=True, blank=True, max_digits=10, decimal_places=2)

    def __str__(self):
        return str(self.producto)

class metodos_de_pago(models.Model):
    forma_pago = models.CharField("Método de pago",max_length=150,null=True, blank=True)

    def __str__(self):
        return self.forma_pago

class Order(models.Model):
    cliente = models.ForeignKey(MyUser, on_delete=models.CASCADE, null=True, blank=True)
    metodo_pago = models.ForeignKey(metodos_de_pago, null=True, blank=True, on_delete=models.PROTECT)        
    fecha_pedido = models.DateTimeField("Fecha del pedido",auto_now_add=True)
    serv_pedido = models.ForeignKey(servicios,  null=True, blank=True, on_delete=models.PROTECT)
    prod_pedido = models.ForeignKey(productos, null=True, blank=True, on_delete=models.PROTECT)
    price = models.DecimalField ("Precio total",null=True, blank=True, max_digits=10, decimal_places=2)
    cantidad = models.DecimalField ("Cantidad de productos pedidos",null=True, blank=True, max_digits=10, decimal_places=0)
    fecha_inicio = models.DateField("Fecha de inicio del servicio",null=True, blank=True)
    fecha_fin = models.DateField("Fecha de finalización del servicio",null=True, blank=True)
   
    def __str__(self):
        return '%s - %s' % (self.cliente, self.fecha_pedido)

























