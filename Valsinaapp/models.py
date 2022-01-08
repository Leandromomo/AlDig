from django.db import models
from django.contrib.auth.models import User



class Publicidad(models.Model):
    nombrenegocio=models.CharField(max_length=100)
    Autor=models.ForeignKey(User, on_delete=models.CASCADE)
    imagen=models.ImageField(upload_to="publicidadimg", null=True, blank=True)
    slogan=models.CharField(max_length=300)
    direccion=models.CharField(max_length=80)
    telefono=models.CharField(max_length=20)
    web=models.CharField(max_length=80)    
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now_add=True)


    class Meta:
        
        verbose_name='publicidad'
        verbose_name_plural='publicidades'

        def __str__(self):
            return self.nombrenegocio