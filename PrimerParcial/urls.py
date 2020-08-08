"""PrimerParcial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from Models.Inscripcion.views import OperaForms
from Models.Grado.views import FormularioGradoViews
from Views.HomeView import HomeView
from Models.Alumno.views import FormularioAlumnoView

urlpatterns = [
   # path('admin/', admin.site.urls),
     #URL DE INSCRIPCIONES
     path("Inscripcion",OperaForms.mostrarforms, name="mostrarforms"),
     path("INGRESARINS",OperaForms.agregarforms, name="guardarforms"),
     path("LISTAINSC", OperaForms.listaforms, name="listaforms"),
     path("LISTAINSC/<id>", OperaForms.eliminarforms, name="eliminarforms"),
     path("MODIFICAR/<id>", OperaForms.modificarforms, name="modificarforms"),

     #URL DE GRADOS
     path("registrarGrado/", FormularioGradoViews.indexg, name='registrarGrado'),
     path("guardarGrado/", FormularioGradoViews.procesar_formulariog, name='guardarGrado'),
     path("listarGrados/", FormularioGradoViews.listar_grados, name='listarGrados'),
     path("listarGrados/<id>",FormularioGradoViews.eliminarG, name="ELIMINAR"),
     path("editarGrados/<id>",FormularioGradoViews.modificarG, name="MODIFICARG"),

# URL DE ALUMNOS
     path("registrarAlumno/", FormularioAlumnoView.index, name='registrarAlumno'),
     path("guardarAlumno/", FormularioAlumnoView.procesar_formulario, name='guardarAlumno'),
     path("listarAlumnos/", FormularioAlumnoView.listar_alumnos, name='listarAlumnos'),
     path("listarAlumnos/<id>",FormularioAlumnoView.eliminarA, name="ELIMINAROBEJTO"),
     path("editarAlumnos/<id>",FormularioAlumnoView.modificarA, name="MODIFICARLU"),

     path('', HomeView.home, name='home'),
]
