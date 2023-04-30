from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario


def cursoFormulario(request):
    if request.method == "POST":
           # Aqui me llega la informacion del html
        miFormulario = CursoFormulario(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            curso = Curso(int(informacion['id']), str(
            informacion['nombre']), int(informacion['curso']))
            curso.save()
            return render(request, "App1/inicio.html")
    else:
        miFormulario = CursoFormulario()

    return render(request, "AppCoder/cursoFormulario.html", {"miFormulario": miFormulario})

def curso(self):
    curso = Curso(nombre="Desarroyo Web", camada="12345")
    curso.save()
    documentoDeTexto = f"--->Curso: {curso.nombre}  Camada: {curso.camada}"
    return HttpResponse(documentoDeTexto)

def inicio(request):
    return render(request, "AppCoder/inicio.html")
def cursos(request):
    return render(request, "AppCoder/cursos.html")
def profesores(request):
    return render(request, "AppCoder/profesores.html")
def estudiantes(request):
    return render(request, "AppCoder/estudiantes.html")
def entregables(request):
    return render(request, "AppCoder/entregables.html")