from django.http import HttpRequest
from django.shortcuts import render, redirect

from Models.Grado.FormsG import FormularioGrado
from Models.Grado.models import Grado

class FormularioGradoViews(HttpRequest):

    # GRADO

    def indexg(request):
        grado = FormularioGrado()
        return render(request, "GradoIndex.html", {"form": grado})

    def procesar_formulariog(request):
        grado = FormularioGrado(request.POST)
        if grado.is_valid():
            grado.save()
            grado = FormularioGrado()
        return render(request, "GradoIndex.html", {"form": grado, "mensaje": 'OK'})

    def listar_grados(request):
        grados = Grado.objects.all()
        return render(request, "ListaGrados.html", {"lb_grados": grados})

    def eliminarG(request, id):
        Grado.objects.filter(id_grado=id).delete()
        return redirect(to="listarGrados")

    def modificarG(request, id):
        MODG = Grado.objects.get(id_grado=id)
        data = {
            'form': FormularioGrado(instance=MODG)
        }
        if request.method == 'POST':
            formulario = FormularioGrado(data=request.POST, instance=MODG)
            if formulario.is_valid():
                formulario.save()
                data['mensaje'] = "Se ha actualizado el registro."
                data['form'] = formulario
        return render(request, 'Modificar_grado.html', data)