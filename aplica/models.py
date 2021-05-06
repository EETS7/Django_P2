from django.db import models
class uno(models.Model):
    Nombre=models.CharField(max_length=30)
    Numero=models.CharField(max_length=10)
    Intentos=models.CharField(max_length=10)
# Create your models here.
