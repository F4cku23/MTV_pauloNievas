from cgitb import text
from django.db import models

# Create your models here.

class Familiar(models.Model):
    nombre=models.CharField(max_length=35)
    edad=models.PositiveBigIntegerField()
    nacimiento=models.DateField()
    
    def __str__(self):
        texto="{0} ({1})"
        return texto.format(self.nombre, self.edad, self.nacimiento)