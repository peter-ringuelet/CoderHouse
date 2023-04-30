from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse

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