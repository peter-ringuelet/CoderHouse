from django.shortcuts import render
from .models import Familiar

# Create your views here.
def listar_familiares(request):
    familiares = Familiar.objects.all()
    return render(request, 'familiares/listar_familiares.html', {'familiares': familiares})
