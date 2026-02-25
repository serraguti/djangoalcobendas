from django.shortcuts import render
from television import models as md

# Create your views here.
def index(request):
    return render(request, "index.html")

def series(request):
    service = md.ServiceSeries()
    listaSeries = service.getSeries()
    informacion = {
        "listaseries": listaSeries
    }
    return render(request, "series.html", informacion)

def personajes(request):
    if ('idserie' in request.GET):
        service = md.ServiceSeries()
        idserie = int(request.GET["idserie"])
        personajes = service.getPersonajesSerie(idserie)
        informacion = {
            "personajes": personajes
        }
        return render(request, "personajes.html", informacion)
    else: 
        return render(request, "personajes.html")