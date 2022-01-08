from django.shortcuts import render, HttpResponse
from .models import Publicidad

# Create your views here.
def home(request):
    publicidades=Publicidad.objects.all()
    
    return render(request,"Alsina3dd/home.html",{"publicidades":publicidades})