from django.urls import path
from .views import Home, Agendar , RevisarAgendas


urlpatterns = [
    path('', Home, name="home"),
    path('agendar/', Agendar, name="agendar"),
    path('reservas/', RevisarAgendas, name="revisarReserva")
]
