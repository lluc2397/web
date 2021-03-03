from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth import get_user_model

MyUser = get_user_model()

class generos(models.Model):
    generos_temas= models.CharField("Géneros de los temas",max_length=150,null=True, blank=True)

    def __str__(self):
        return self.generos_temas

class cursos(models.Model):
    titulo = models.CharField(max_length=150,null=True, blank=True)
    resumen = RichTextField(null=True, blank=True)
    genero = models.ForeignKey(generos, blank=True, on_delete=models.PROTECT, null=True)    
    pdf_curso = models.FileField(upload_to='curso/',null=True, blank=True)
    alumnos = models.ManyToManyField(MyUser, blank=True)
    foto = models.ImageField(upload_to='curso/',null=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_actualización = models.DateTimeField('Fecha actualización', null=True, blank=True )

    def __str__(self):
        return self.titulo

class Modulo (models.Model):
    nombre_modulo = models.CharField(max_length=150,null=True, blank=True)
    curso_relacionado = models.ForeignKey(cursos, null=True, blank=True, on_delete=models.PROTECT)
    resumen = RichTextField(null=True, blank=True)
    contenido_modulo = RichTextField(null=True, blank=True)
    audio = models.FileField(upload_to='curso/',null=True, blank=True)
    pdf_modulo = models.FileField(upload_to='curso/',null=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)
    fecha_actualización = models.DateTimeField('Fecha actualización', null=True, blank=True )

    def __str__(self):
        return self.nombre_modulo

class talleres(models.Model):
    titulo = models.CharField(max_length=150,null=True, blank=True)
    resumen = RichTextField(null=True, blank=True)
    genero = models.ForeignKey(generos, blank=True, on_delete=models.PROTECT, null=True)
    herramienta = models.FileField(upload_to='taller/',null=True, blank=True)
    contenido_taller = RichTextField(null=True, blank=True)
    audio = models.FileField(upload_to='taller/',null=True, blank=True)
    pdf_ejercicio = models.FileField(upload_to='taller/',null=True, blank=True)
    pdf_correcion = models.FileField(upload_to='taller/',null=True, blank=True)
    alumnos = models.ManyToManyField(MyUser, blank=True)
    curso_relacionado = models.OneToOneField(cursos, null=True, blank=True, on_delete=models.PROTECT)
    image = models.ImageField (upload_to='taller/',null=True, blank=True)
    fecha_publicacion = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
