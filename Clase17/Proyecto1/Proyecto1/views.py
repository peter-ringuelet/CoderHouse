from django.http import HttpResponse
import datetime
from django.template import Template, Context, loader


def saludo(request):
    return HttpResponse("Hola Django - Coder")


def segunda_vista(request):
    return HttpResponse("<br>Segunda vista!")

def fechaActual(request):
    fecha = datetime.datetime.now()
    texto = f"Fecha actual: {fecha}"
    return HttpResponse(texto)

def miNombre(self,nombre):
    texto = f"Mi nombre es {nombre}"
    return HttpResponse(texto)

def probandoTemplate(self):
    nom = "Pedro"
    ap = "Ringuelet"
    listaDeNotas = [2,2,3,7,2,5]
    diccionario = {"nombre":nom, "apellido":ap, "hoy":datetime.datetime.now(), "notas":listaDeNotas}
    plantilla = loader.get_template('template1.html')
    documento = plantilla.render(diccionario)
    return HttpResponse(documento)
