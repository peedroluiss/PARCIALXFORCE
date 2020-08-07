from django.db import models

# Create your models here.
class Grado(models.Model):

    id_grado = models.AutoField(primary_key=True)
    Nombre = models.CharField(max_length=30)
    Descripcion = models.CharField(max_length=30)
    Catedratico = models.CharField(max_length=30)