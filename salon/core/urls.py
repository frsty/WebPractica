from django.urls import path
from .views import Home, Agendar


urlpatterns = [
    path('', Home, name="home"),
    path('agendar/', Agendar, name="agendar"),
]
