from django import forms
from django.forms import ModelForm
from .models import Activo, Cartera
import datetime

class AgregarActivo (forms.ModelForm):
    class Meta:
        model = Activo
        fields = "__all__"

class ModCartera (forms.ModelForm):
    fecha_movimiento = forms.DateField(initial=datetime.date.today)


    class Meta:
        model = Cartera
        fields = [
            "activo",
            "nombre_activo",
            "nombre_activo",
            "ticker_accion",
            "rendimiento",
            "valor",
            "cantidad",
            "movimiento",
            "fecha_movimiento",
            "observacion",
        ]