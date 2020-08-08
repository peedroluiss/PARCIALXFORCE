from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse
from django.template.loader import get_template

from Models.Inscripcion.Forms import FormsInscripcion, Inscripcion
from Models.Grado.FormsG import FormularioGrado

class OperaForms(HttpRequest):

    def  mostrarforms (request):
        A = FormsInscripcion()
        return render(request,'Inscripcion.html',{'form':A})


    def  agregarforms (request):
        B = FormsInscripcion(request.POST)
        if B.is_valid():
            B.save()
            B= FormsInscripcion()
        return render(request,'Inscripcion.html', {'form': B, "mensaje": "Ok"})

    def listaforms(request):
        inscripcion = Inscripcion.objects.all()
        return render(request, "Listainscrip.html", {"lb_inscripcion": inscripcion})

    def eliminarforms(request, id):
        Inscripcion.objects.filter(id_ins=id).delete()

        return redirect(to="listaforms")

    def  editarforms(request, id):
        C = FormsInscripcion.object.get(id_ins=id)
        if request.method == 'GET':
            form =  FormsInscripcion(instance= C)

        else:
             form = FormsInscripcion(request.POST, instace= C)
             if form.is_valid():
                 form.save()
             return render (request, 'Listainscrip.html', {'form':form})

    def modificarforms(request, id):
        MODIFI = Inscripcion.objects.get(id_ins=id)
        data = {
            'form': FormsInscripcion(instance=MODIFI)
        }
        if request.method == 'POST':
            formulario = FormsInscripcion(data=request.POST, instance=MODIFI)
            if formulario.is_valid():
                formulario.save()
                data['mensaje'] = "Se ha actualizado el registro."
                data['form'] = formulario
        return render(request, 'Modificaralumno.html', data)


