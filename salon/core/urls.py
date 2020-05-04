from django.urls import path
from .views import Home, Agendar #, registro_usuario


urlpatterns = [
    path('', Home, name="home"),
    path('agendar/', Agendar, name="agendar"),
    #path('registro/', registro_usuario, name="registro_usuario")
]
