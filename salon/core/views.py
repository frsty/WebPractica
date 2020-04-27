from django.shortcuts import render
from .models import Servicio, Reserva

# Create your views here.

def Home(request):
    #para ver los precios en el home 
    serv = Servicio.objects.all()
    data = {
        'servicio':serv
    }
    return render(request, 'core/home.html', data)
    

def Agendar(request):
    serv = Servicio.objects.all()
    data = {
        'servicio':serv
    }

    if request.POST:
        
        agenda = Reserva()
        nam = request.POST.get('txtNombre')
        last = request.POST.get('txtApellido')
        agenda.nombre = nam + last
        agenda.telefono = request.POST.get('txtTelefono')
        agenda.email = request.POST.get('txtEmail')
        agenda.hora = request.POST.get('txtHora')
        agenda.fecha = request.POST.get('txtFecha')
        service = Servicio()
        service.id = request.POST.get('cbService')
        agenda.servi = service

        agenda.save()

    return render(request, 'core/agendar.html',data)


    

