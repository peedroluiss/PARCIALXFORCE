from django.forms import ModelForm
from django.forms import  DateInput
from Models.Inscripcion.models import Inscripcion

class FormsInscripcion(ModelForm):


    class Meta:
        model = Inscripcion
        fields = [
            'fecha',
            'alumno_id_alumno',
            'grado_id_grado',
            'seccion_id_seccion',


        ]

        labels = {
            'fecha': 'Fecha de Inscripcion',
            'alumno_id_alumno': 'Nombre de Alumno',
            'grado_id_grado': 'Grado ',
            'seccion_id_seccion': 'Seccion',


        }
        widgets = {"fecha": DateInput(attrs={'type': 'date'})}