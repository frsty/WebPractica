from django.urls import path , include
from .views import Home, Agendar , RevisarAgendas


urlpatterns = [
    path('', Home, name="home"),
    path('agendar/', Agendar, name="agendar"),
    path('reservas/', RevisarAgendas, name="revisarReserva"),
    path('',include('pwa.urls')),
]
