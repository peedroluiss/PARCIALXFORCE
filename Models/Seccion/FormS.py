from django.forms import forms
from django.forms import ModelForm
from Models.Seccion.models import Seccion


class FormularioSeccion(ModelForm):

    class Meta:
        model = Seccion
        fields = '__all__'
