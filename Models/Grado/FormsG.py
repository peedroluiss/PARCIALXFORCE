from django.forms import forms
from django.forms import ModelForm
from Models.Grado.models import Grado




class FormularioGrado(ModelForm):

    class Meta:
        model = Grado
        fields = '__all__'
