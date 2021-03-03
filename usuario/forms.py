from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import MyUser
from django import forms
from django.core.exceptions import ValidationError
from django.forms.fields import URLField
from ckeditor.fields import RichTextField
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from phonenumber_field.widgets import PhoneNumberPrefixWidget

class MyUserCreationForm(UserCreationForm):
    username = forms.CharField(label='Nombre de usuario', widget=forms.TextInput,  help_text='Introduce tu nombre de usuario')
    email = forms.EmailField(label = 'Correo electrónico', widget=forms.EmailInput)
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Confirmación de las contraseñas', widget=forms.PasswordInput)
     
    class Meta:
        model = MyUser
        fields = ['username', 'email', 'password1', 'password2', ]
    
    def clean_username(self):
        username = self.cleaned_data['username'].lower()
        qs = MyUser.objects.filter(username=username)
        if qs.exists():
            raise forms.ValidationError('Este usuario ya está siendo usado. Ingresa en tu cuenta o prueba con otro nombre de usuario.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        qs = MyUser.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError('Este correo electrónico ya está siendo usado. Ingresa en tu cuenta o prueba con otro email.')
        return email

    def clean_password2(self):
        password1 = self.cleaned_data['password1']
        password2 = self.cleaned_data['password2']

        if (password1 and password2) and (password1 != password2):
            raise forms.ValidationError('Las contraseñas no coinciden. Inténtalo de nuevo.')
        return password2

    def save(self, commit=True):
        user = super(MyUserCreationForm, self).save(commit=False)
        user.username = self.cleaned_data['username']
        user.email = self.cleaned_data['email']
        user.password = self.cleaned_data["password1"]
        if commit:
            user.save()
        return user

