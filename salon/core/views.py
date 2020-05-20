from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from .models import Servicio, Reserva, TipoServicio
from django.contrib.auth.decorators import login_required 
from .forms import CustomUserForm, ContactForm
from django.contrib.auth import login, authenticate
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt




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
        email_mensaje = '''
            Nombre: %s 
            telefono de contacto: %s 
            duda: %s 
            Correo de contacto %s
            ''' %(form_nombre, form_telefono, form_mensaje, form_email)
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
    
    tipoSs = TipoServicio.objects.all()
    serv = Servicio.objects.none()

   
   
    data = {}
    try:
        action = request.POST['action']
        if action == 'buscar_TipoServicio':
            data = []
            for i in Servicio.objects.filter(id=request.POST['id']):
                data.append({'id': i.id , 'name': i.nombre})
                
        else:
            data['error'] = 'Ha ocurrido un error'
    except Exception as e:
        data['error'] = str(e)
        
    response = JsonResponse(data, safe=False)
        

    if request.POST:
        
        agenda = Reserva()
        nam = request.POST.get('txtNombre')
        last = request.POST.get('txtApellido')
        agenda.nombre =  request.POST.get('txtNombre') +' '+request.POST.get('txtApellido')
        agenda.telefono = request.POST.get('txtTelefono')
        agenda.email = request.POST.get('txtEmail')
        agenda.hora = request.POST.get('txtHora')
        agenda.fecha = request.POST.get('txtFecha')
       
        #saca el servicio
        service = Servicio()
        service.id = request.POST.get('cbTipoService')
        agenda.servi = service.id

         #saca el tipo de servicio
        tipoServ = TipoServicio()
        tipoServ.id = request.POST.get('cbService')
        agenda.tipo = tipoServ.id
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

    datosRetorno = {
        'servicio':serv,
        'tipo': tipoSs,
        'json':response.content
        
    }
    
    return render(request, 'core/agendar.html',datosRetorno)
