from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#Creamos metodos para dibujar las vistas
def index(request):
    return render(request, "paginas/index.html")

def prueba(request):
    return render(request, "paginas/prueba.html")

def peliculas(request):
    return render(request, "paginas/peliculas.html")

def futbol(request):
    informacion = {
        "equipo": "Real Madrid"
    }
    return render(request, "paginas/futbol.html", informacion)

def nombres(request):
    lista = ["Adrian", "Lucia", "Antonia", "Diana", "Miriam"]
    #Me gustaria enviar el nombre y la edad...
    listapersonas = [
        { "nombre": "Adrian", "edad": 26 },
        { "nombre": "Lucia", "edad": 23 },
        { "nombre": "Antonia", "edad": 55 }
    ]
    #La informacion la debemos enviar mediante diccionario
    informacion = {
        "listanombres": lista,
        "listapersonas": listapersonas
    }
    return render(request, "paginas/nombres.html", informacion)

def mascotas(request):
    listamascotas = [
        {
            "nombre": "Wall-e",
            "raza": "limpiador",
            "edad": 17
        },
        {
            "nombre": "Eva",
            "raza": "exploradora",
            "edad": 16
        },
        {
            "nombre": "Rafiki",
            "raza": "brujo",
            "edad": 22
        },
        {
            "nombre": "Olaf",
            "raza": "nieve",
            "edad": 12
        }
    ]
    informacion = {
        "listamascotas": listamascotas
    }
    return render(request, "paginas/mascotas.html", informacion)