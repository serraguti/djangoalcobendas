from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Creamos metodos para dibujar las vistas
def index(request):
    return HttpResponse("Mi primera pagina Django")

def prueba(request):
    return HttpResponse("Probando probando...")
