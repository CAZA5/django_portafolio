from django.shortcuts import render
from .models import proyecto
# Create your views here.
def portafolio(request):
    # traer todos los objetos de la clase proyecto
    proyectos = proyecto.objects.all()
    return render(request, "portafolio_app/portafolio.html", {"proyectos": proyectos})

