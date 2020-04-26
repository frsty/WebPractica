from django.shortcuts import render
from .models import Servicio

# Create your views here.

def Home(request):
    #para ver los precios en el home 
    serv = Servicio.objects.all()
    data = {
        'servicio':serv
    }
    return render(request, 'core/home.html', data)
    

def Agendar(request):
    return render(request, 'core/agendar.html')


    

