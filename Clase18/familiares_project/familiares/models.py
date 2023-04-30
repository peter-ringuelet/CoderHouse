from django.db import models

# Create your models here.
class Familiar(models.Model):
    nombre = models.CharField(max_length=100)
    relacion = models.CharField(max_length=100)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return self.nombre
