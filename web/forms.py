from django.forms import ModelForm
from .models import CommentWeb
from django import forms

class CommentWebForm(forms.ModelForm):
    content = forms.CharField ( widget=forms.Textarea(attrs={'placeholder':"¿Qué opinas?"}))
    class Meta:
        model = CommentWeb
        fields = ['content']