from django.http import HttpRequest
from django.shortcuts import render, redirect

from Models.Seccion.FormS import  FormularioSeccion
from Models.Seccion.models import Seccion

class FormularioSeccionViews(HttpRequest):

    # SECCION

    def indexs(request):
        seccion = FormularioSeccion()
        return render(request, "SeccionIndex.html", {"form": seccion})

    def procesar_formularioss(request):
        seccion = FormularioSeccion(request.POST)
        if seccion.is_valid():
            seccion.save()
            seccion = FormularioSeccion()
        return render(request, "SeccionIndex.html", {"form": seccion, "mensaje": 'OK'})

    def listar_secciones(request):
        seccion = Seccion.objects.all()
        return render(request, "ListaSecciones.html", {"lb_secciones": seccion})

    def eliminarS(request, id):
        Seccion.objects.filter(id_seccion=id).delete()
        return redirect(to="listarseccion")

    def modificarS(request, id):
        MODS = Seccion.objects.get(id_seccion=id)
        data = {
            'form': FormularioSeccion(instance=MODS)
        }
        if request.method == 'POST':
            formulario = FormularioSeccion(data=request.POST, instance=MODS)
            if formulario.is_valid():
                formulario.save()
                data['mensaje'] = "Se ha actualizado el registro."
                data['form'] = formulario
        return render(request, 'Modificar_seccion.html', data)
