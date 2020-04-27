from django.shortcuts import render, redirect
from .models import Servicio, Reserva
from django.contrib.auth.decorators import login_required 
from .forms import CustomUserForm
from django.contrib.auth import login, authenticate


# Create your views here.

def Home(request):
    #para ver los precios en el home 
    serv = Servicio.objects.all()
    data = {
        'servicio':serv
    }
    return render(request, 'core/home.html', data)
    
@login_required
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


def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            #login en la pagina altiro
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']
            user = authenticate(username = username, password = password)
            login(request, user)

            return redirect(to='home')

    return render(request, 'registration/registrar.html',data)

