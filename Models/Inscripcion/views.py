from django.shortcuts import render
from django.http import HttpRequest
from Models.Inscripcion.Forms import  FormsInscripcion, Inscripcion

class OperaForms(HttpRequest):

    def  mostrarforms (request):
        A = FormsInscripcion()
        return render(request,'Inscripcion.html',{'form':A})

