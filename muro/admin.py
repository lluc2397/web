from django.contrib import admin
from .models import (Libros, Autores, servicios, productos,
 Order, metodos_de_pago)

admin.site.register(metodos_de_pago)
admin.site.register(servicios)
admin.site.register(productos)
admin.site.register(Order)
admin.site.register(Libros)
admin.site.register(Autores)
