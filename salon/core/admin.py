from django.contrib import admin
from .models import *

# Register your models here.

class ReservaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'telefono','email','fecha','hora','servi']
    search_fields = ['email','nombre']
    list_filter = ['servi']
    list_per_page = 10


admin.site.register(Servicio)
admin.site.register(Reserva, ReservaAdmin)
