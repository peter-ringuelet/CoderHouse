from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_familiares, name='listar_familiares'),
]
