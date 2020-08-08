from django.http import HttpResponse
from django.template.loader import get_template


class HomeView():

    def home(self):
        plantilla = get_template('Inicio.html')
        return HttpResponse(plantilla.render())

