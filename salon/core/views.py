from django.shortcuts import render
from .models import Servicio

# Create your views here.

def home(request):
    return render(request,'core/home.html')

def agendar(request):
    return render(request, 'core/agendar.html')

def ListaServicio(request):
    serv = Servicio.objects.all()
    data = {
        'servicio':serv
    }
    return render(request,'core/home.html', data)