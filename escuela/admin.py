from django.contrib import admin
from .models import talleres, cursos, generos, Modulo

admin.site.register(talleres)
admin.site.register(cursos)
admin.site.register(generos)
admin.site.register(Modulo)
