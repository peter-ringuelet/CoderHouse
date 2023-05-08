from django.shortcuts import render
from django.http import HttpResponse
from AppSACCOM.models import *
from AppSACCOM.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.urls import reverse_lazy
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from AppSACCOM.forms import UserRegisterForm
from django.contrib.auth.views import LogoutView



# Create your views here.

def actividad(request):
 
      if request.method == "POST":
 
            miFormulario = ActividadFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  actividad = Actividad(nombre=informacion["nombre"], fecha_inicio=informacion["fecha_inicio"])
                  actividad.save()
                  return render(request, "AppSACCOM/inicio.html")
      else:
            miFormulario = ActividadFormulario()
 
      return render(request, "AppSACCOM/actividades.html", {"miFormulario": miFormulario})


def comision(request):
 
      if request.method == "POST":
 
            miFormulario = ComisionFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  comision = ComisionDirectiva(nombre=informacion["nombre"], apellido=informacion["apellido"], dni=informacion["dni"], cargo=informacion["cargo"])
                  comision.save()
                  return render(request, "AppSACCOM/inicio.html")
      else:
            miFormulario = ComisionFormulario()
 
      return render(request, "AppSACCOM/comision.html", {"miFormulario": miFormulario})


def socio(request):
 
      if request.method == "POST":
 
            miFormulario = SocioFormulario(request.POST) # Aqui me llega la informacion del html
            print(miFormulario)
 
            if miFormulario.is_valid:
                  informacion = miFormulario.cleaned_data
                  socio = Socio(nombre=informacion["nombre"], apellido=informacion["apellido"], dni=informacion["dni"])
                  socio.save()
                  return render(request, "AppSACCOM/inicio.html")
      else:
            miFormulario = SocioFormulario()
 
      return render(request, "AppSACCOM/socios.html", {"miFormulario": miFormulario})


def inicio(request):
      return render(request, "AppSACCOM/inicio.html")

def buscar(request):
      if request.GET['nombre']:
            nombre = request.GET['nombre']
            actividades = Actividad.objects.filter(nombre__icontains=nombre)
            return render(request, "AppSACCOM/resultadosBusqueda.html", {"actividades": actividades, "nombre":nombre})
      else:
            respuesta = "No existen datos"
      
      return HttpResponse(respuesta)


'''def leerSocios(request):
    socios = Socio.objects.all()  # Trae todos los socios
    contexto = {"socios": socios}
    return render(request, "AppSACCOM/leerSocios.html", contexto)


def eliminarSocio(request, socio_dni):
      socio = Socio.objects.get(dni = socio_dni)
      socio.delete()

      #vuelvo al menu
      socios = Socio.objects.all() #Trae todos los profesores
      contexto = {"socios":socios}
      return render(request, "AppSACCOM/leerSocios.html", contexto)


def editarSocio(request, socio_dni):
    # Recibe el dni del socio que vamos a modificar
    socio = Socio.objects.get(dni=socio_dni)
    # Si es metodo POST hago lo mismo que el agregar
    if request.method == 'POST':
        # aquí mellega toda la información del html
        miFormulario = SocioFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:  # Si pasó la validación de Django
            informacion = miFormulario.cleaned_data

            socio.nombre = informacion['nombre']
            socio.apellido = informacion['apellido']
            socio.dni = informacion['dni']
            socio.save()

            # Vuelvo al inicio o a donde quieran
            return render(request, "AppSACCOM/inicio.html")
    # En caso que no sea post
    else:
        # Creo el formulario con los datos que voy a modificar
        miFormulario = SocioFormulario(initial={'nombre': socio.nombre, 'apellido': socio.apellido,
                                                   'dni': socio.dni})
    # Voy al html que me permite editar
    return render(request, "AppSACCOM/editarSocio.html", {"miFormulario": miFormulario, "socio_dni": socio_dni})

'''
# ----------Actividad----------
class ActividadList(ListView):
    model = Actividad
    template_name = "AppSACCOM/actividad_list.html"

class ActividadDetalle(DetailView):
    model = Actividad
    template_name = "AppSACCOM/actividad_detalle.html"

class ActividadCreacion(CreateView):
    model = Actividad
    success_url = "/AppSACCOM/actividad/list"
    fields = ['nombre', 'fecha_inicio']

class ActividadUpdate(UpdateView):
    model = Actividad
    success_url = "/AppSACCOM/actividad/list"
    fields = ['nombre', 'fecha_inicio']

class ActividadDelete(DeleteView):
    model = Actividad
    success_url = "/AppSACCOM/actividad/list"

#----------Socio----------
class SocioList(ListView):
    model = Socio
    template_name = "AppSACCOM/socio_list.html"


class SocioDetalle(DetailView):
    model = Socio
    template_name = "AppSACCOM/socio_detalle.html"


class SocioCreacion(CreateView):
    model = Socio
    success_url = "/AppSACCOM/socio/list"
    fields = ['nombre', 'apellido', 'dni']


class SocioUpdate(UpdateView):
    model = Socio
    success_url = "/AppSACCOM/socio/list"
    fields = ['nombre', 'apellido', 'dni']


class SocioDelete(DeleteView):
    model = Socio
    success_url = "/AppSACCOM/socio/list"


# ----------Comision----------
class ComisionList(ListView):
    model = ComisionDirectiva
    template_name = "AppSACCOM/comision_list.html"
    context_object_name = 'comision'


class ComisionDetalle(DetailView):
    model = ComisionDirectiva
    template_name = "AppSACCOM/comision_detalle.html"
    context_object_name = 'comision'


class ComisionCreacion(CreateView):
    model = ComisionDirectiva
    success_url = "/AppSACCOM/comision/list"
    fields = ['nombre', 'apellido', 'dni', 'cargo']
    context_object_name = 'comision'


class ComisionUpdate(UpdateView):
    model = ComisionDirectiva
    success_url = "/AppSACCOM/comision/list"
    fields = ['nombre', 'apellido', 'dni', 'cargo']
    template_name = 'AppSACCOM/comision_form.html'
    context_object_name = 'comision'


class ComisionDelete(DeleteView):
    model = ComisionDirectiva
    success_url = "/AppSACCOM/comision/list"
    template_name = 'AppSACCOM/comision_confirm_delete.html'
    context_object_name = 'comision'
    
#---------LogIn---------
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            user = authenticate(username= usuario, password=contrasenia)
            if user is not None:
                login(request, user)
                return render(request, "AppSACCOM/inicio.html", {"mensaje":f"Bienvenido {usuario}"})
            else:
                return render(request, "AppSACCOM/inicio.html", {"mensaje":"Datos incorrectos"})
        else:
            return render(request, "AppSACCOM/inicio.html", {"mensaje":"Formulario erroneo"})
    form = AuthenticationForm()
    return render(request, "AppSACCOM/login.html", {"form": form})

#----------Register----------
def register(request):
      if request.method == 'POST':
            #form = UserCreationForm(request.POST)
            form = UserRegisterForm(request.POST)
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"AppSACCOM/inicio.html" ,  {"mensaje":"Usuario Creado :)"})
      else:
            #form = UserCreationForm()       
            form = UserRegisterForm()     
      return render(request,"AppSACCOM/registro.html" ,  {"form":form})
