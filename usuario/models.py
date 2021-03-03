from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
from django_countries.fields import CountryField
from django.db.models import URLField
from django.core.mail import send_mail
from phonenumber_field.modelfields import PhoneNumberField

class CustomAccountManager(UserManager):

    def create_superuser(self, username, email, password, **other_fields):

        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        if other_fields.get('is_staff') is not True:
            raise ValueError(
                'Superuser must be assigned to is_staff=True.')
        if other_fields.get('is_superuser') is not True:
            raise ValueError(
                'Superuser must be assigned to is_superuser=True.')

        return self.create_user(username, email, password, **other_fields)

class MyUser(AbstractUser):
    first_name = models.CharField("Nombre", max_length=150, blank=True)
    last_name = models.CharField("Apellidos", max_length=150, blank=True)
    pais = CountryField("País de origen", null=True, blank=True)    
    telefono = PhoneNumberField("Número telefónico", null=True, blank=True)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)      
    
    def __str__(self, *args, **kwargs):
        return self.username
    
    def email_user(self, subject, message):
        send_mail(
            subject,
            message,
            'noreply@inversionesyfinanzas.com',
            [self.email],
            fail_silently=False,
        )