from django.contrib.auth.forms import UserChangeForm
from .models import Perfil
from django import forms
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
from django_countries.fields import CountryField
from django_countries.widgets import CountrySelectWidget
from django.contrib.auth import get_user_model

MyUser = get_user_model()

class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = MyUser
        fields = ['username', 'first_name', 'pais']


class ProfileUpdateForm(forms.ModelForm):


    class Meta:
        model = Perfil
        fields = [
            'edad',
            'ciudad',
            'foto_perfil',
            'bio',
            'facebook',
            'twitter',
            'tiktok',
            'instagram',
            'pinterest',
        ]