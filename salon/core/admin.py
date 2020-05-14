from django.contrib import admin
from .models import Reserva, Servicio, TipoServicio

# Register your models here.

class ReservaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono','email','fecha','servi','tipo']
    search_fields = ['email','nombre']
    list_filter = ['tipo']
    list_per_page = 10

class ServicioAdmin(admin.ModelAdmin):
    list_display = ['nombre','precio']


admin.site.register(Servicio, ServicioAdmin)
admin.site.register(Reserva, ReservaAdmin)
admin.site.register(TipoServicio)

