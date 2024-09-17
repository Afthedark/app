from django.db import models

from django.contrib.auth.models import User #para importar el modelo User de django.contrib.auth.models

#Esto se podra heredar a otros modelos

# Create your models here.
class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True) #Es un campo de tipo booleano
    fc = models.DateTimeField(auto_now_add=True) #Es un campo de tipo fecha y hora en tiempo real
    fm = models.DateTimeField(auto_now=True)
    uc = models.ForeignKey(User, on_delete=models.CASCADE)
    um = models.IntegerField(blank=True, null=True)

    class Meta: #Para que el modelo sea abstracto y no se cree en la base de datos de django
        abstract=True