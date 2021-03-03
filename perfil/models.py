from django.db import models
from ckeditor.fields import RichTextField
from django_countries.fields import CountryField
from PIL import Image
from django.contrib.auth import get_user_model
from datetime import date

MyUser = get_user_model()

class Perfil (models.Model):
    user = models.OneToOneField(MyUser,on_delete=models.CASCADE)    
    edad = models.DateField("Fecha de nacimiento", null=True, blank=True)
    ciudad = models.CharField("Ciudad de origen", max_length=150,null=True, blank=True)
    foto_perfil = models.ImageField("Foto de perfil", upload_to='avatar/', default="inversorinteligente.png")
    bio = RichTextField("Descripción", null=True, blank=True)
    facebook = models.CharField("Link de tu Facebook",max_length=3000,  null=True, blank=True)
    twitter = models.CharField("Link de tu Twitter", max_length=3000, null=True, blank=True) 
    tiktok = models.CharField("Link de tu Tiktok", max_length=3000, null=True, blank=True) 
    instagram = models.CharField("Link de tu Instagram", max_length=3000, null=True, blank=True)
    pinterest = models.CharField("Link de tu Pinterest",max_length=3000, null=True, blank=True) 

    def __str__(self):
        return str(self.user)
    
    @property
    def followers(self):
        return Follow.objects.filter(follow_user=self.user).count()

    @property
    def following(self):
        return Follow.objects.filter(user=self.user).count()

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save()

        img = Image.open(self.foto_perfil.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.foto_perfil.path)

class Follow(models.Model):
    user = models.ForeignKey(MyUser, related_name='user', on_delete=models.CASCADE)
    follow_user = models.ForeignKey(MyUser, related_name='follow_user', on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)