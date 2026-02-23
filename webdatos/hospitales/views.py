from django.shortcuts import render
#Agregamos la librería de models.py
from hospitales import models as md

# Create your views here.
def index(request):
    return render(request, "index.html")

def tabladepartamentos(request):
    #Creamos un servicio de departamentos
    service = md.ServiceDepartamentos()
    lista = service.getDepartamentos()
    informacion = {
        "departamentos": lista
    }
    return render (request, "departamentos.html", informacion)

def insertarDepartamento(request):
    if ('cajaid' in request.POST):
        service = md.ServiceDepartamentos()
        id = int(request.POST["cajaid"])
        nom = request.POST["cajanombre"]
        loc = request.POST["cajalocalidad"]
        service.insertarDepartamento(id, nom, loc)
        lista = service.getDepartamentos()
        informacion = {
            "departamentos": lista
        }
        return render (request, "departamentos.html", informacion)        
    else:
        return render(request, "insertardepartamento.html")

def updateDepartamento(request):
    if ('cajaid' in request.POST):
        service = md.ServiceDepartamentos()
        id = (int(request.POST["cajaid"]))
        nom = request.POST["cajanombre"]
        loc = request.POST["cajalocalidad"]
        service.updateDepartamento(id, nom, loc)
        lista = service.getDepartamentos()
        informacion = {
            "departamentos": lista
        }
        return render (request, "departamentos.html", informacion)
    else:
        return render(request, "updatedepartamento.html")


