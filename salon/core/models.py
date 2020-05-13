from django.db import models

# Create your models here.

class Servicio(models.Model): 
    nombre = models.CharField(max_length=200)
    precio = models.IntegerField()

    def __str__(self):

        return self.nombre
        
class Reserva(models.Model):
    nombre = models.CharField(max_length=50)
    telefono = models.IntegerField()
    email = models.EmailField(verbose_name="Correo")
    fecha = models.DateField()
    servi = models.ForeignKey(Servicio, on_delete=models.CASCADE, verbose_name="Servicio")
    
    def __str__(self):
        return self.nombre