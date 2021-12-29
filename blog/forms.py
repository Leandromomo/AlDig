from django import forms
from django.forms import fields
from .models import Post, Categoria
from django.forms import ModelForm, Textarea
from django.utils.translation import gettext_lazy as _


class PublicarForm(forms.ModelForm):

    class Meta:
        model= Post
    
        fields = ['titulo', 'contenido', 'imagen', 'categorias']  

       
        





