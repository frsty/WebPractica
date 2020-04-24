from django.db import models

# Create your models here.

class Servicio(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()

class Reserva(models.Model):
    nombre = models.CharField(max_length=200)
    telefono = models.IntegerField()
    email = models.EmailField()
    hora = models.TimeField()
    fecha = models.DateField()
    servi = models.CharField(Servicio, max_length=200)
    
