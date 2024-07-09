from django.db import models

# Create your models here.
class Alumno(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=100, blank=False, null=True)
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=45, blank=True, null=True)
    contraseña = models.CharField(max_length=40)
    ciudad = models.CharField(max_lentgh=40)
    activo = models.IntegerField()
    
    def __str__(self):
        return str(self.nombre)

class productos(models.Model):   
    nombre = models.CharField(primary_key=True)
    descripcion = models.CharField(max_length=150, blank=False, null=True)
    precio = models.CharField(max_length=50)
