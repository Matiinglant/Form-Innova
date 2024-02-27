# En tu archivo models.py
from django.db import models


def user_directory_path(instance, filename):
    
    return 'usuario_{0}/{1}'.format(instance.id, filename)




class InformacionPersonal(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()
    correo_electronico = models.EmailField()
    numero_telefono = models.CharField(max_length=20)
    provincia = models.CharField(max_length=100)
    localidad = models.CharField(max_length=100)
    tiene_cortes_energia = models.CharField(max_length=3, choices=(('Si', 'Si'), ('No', 'No')), blank=True)
    tiene_internet = models.CharField(max_length=3, choices=(('Si', 'Si'), ('No', 'No')), blank=True)
    tiene_computadora = models.CharField(max_length=3, choices=(('Si', 'Si'), ('No', 'No')), blank=True)
    computadora_funciona = models.CharField(max_length=3, choices=(('Si', 'Si'), ('No', 'No')), blank=True)
    tiene_telefono_propio = models.CharField(max_length=3, choices=(('Si', 'Si'), ('No', 'No')), blank=True)
    conocimientos_programacion = models.CharField(max_length=3, choices=(('Si', 'Si'), ('No', 'No')), blank=True)
    archivos_1 = models.FileField(upload_to='archivos/', blank=True)
    archivos_2 = models.FileField(upload_to='archivos/', blank=True)
    archivos_3 = models.FileField(upload_to='archivos/', blank=True)
   
   
   
    def __str__(self):
        return f"{self.nombre} {self.apellido}"
