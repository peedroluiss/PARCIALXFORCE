from django.db import models
from Models.Alumno.models  import  Alumno
from Models.Grado.models  import Grado
from Models.Seccion.models  import Seccion

# Create your models here.

class Inscripcion(models.Model):
    id_ins = models.AutoField(primary_key=True)
    fecha = models.DateField()
    grado_id_grado = models.ForeignKey(Grado, on_delete=models.CASCADE)
    seccion_id_seccion= models.ForeignKey(Seccion, on_delete=models.CASCADE)
    alumno_id_alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_ins