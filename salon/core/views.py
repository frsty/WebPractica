from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Servicio, Reserva
from django.contrib.auth.decorators import login_required 
from .forms import CustomUserForm, ContactForm
from django.contrib.auth import login, authenticate


# Create your views here.

def Home(request):
    #para ver los precios en el home 
    serv = Servicio.objects.all()
    #form contacto
    form = ContactForm(request.POST or None)
    if form.is_valid():
        form_email = form.cleaned_data.get("email")
        form_mensaje = form.cleaned_data.get("mensaje")
        form_nombre = form.cleaned_data.get("nombre")
        form_telefono = form.cleaned_data.get("telefono")
        #esto envia correo ver settings para cambiar correo
        asunto = "Consulta de %s" %(form_nombre)
        email_from = settings.EMAIL_HOST_USER
        email_to = [email_from]
        email_mensaje = '''Nombre: %s telefono de contacto: %s 
            duda: %s Correo de contacto %s''' %(form_nombre, form_telefono, form_mensaje, form_email)
        send_mail(asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently=True)


    data = {
        'servicio':serv,
        'form':form
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

        #ver si funciona esto
        form_nombre = nam + last
        form_email = request.POST.get('txtEmail')
       
        
        email_from = settings.EMAIL_HOST_USER
        email_to = [form_email]
        asunto = 'Reserva'
        email_mensaje ='''Gracias por agendar %s 
        dentro de unos minutos sera contactado para agendar la hora'''%(form_nombre)

        send_mail(asunto,
            email_mensaje,
            email_from,
            email_to,
            fail_silently=True)


    return render(request, 'core/agendar.html',data)
