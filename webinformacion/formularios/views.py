from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "paginas/index.html")

def ejemplo(request):
    return render(request, "paginas/ejemplo.html")

def saludo(request):
    #Siempre con un POST debemos preguntar
    if ('cajanombre' in request.POST):
        #aqui tenemos caja con valor
        dato = request.POST["cajanombre"]
        #Enviamos informacion
        informacion = {
            "nombre": dato
        }
        return render(request, "paginas/saludo.html", informacion)
    else:
        #No enviamos informacion
        return render(request, "paginas/saludo.html")

def SumarNumeros(request):
    if ('cajanum1' in request.POST):
        #Aqui sumamos
        num1 = request.POST["cajanum1"]
        num2 = request.POST["cajanum2"]
        suma = int(num1) + int(num2)
        informacion = {
            "suma": suma
        }
        return render(request, "paginas/sumarnumeros.html", informacion)
    else:
        #No sumamos
        return render(request, "paginas/sumarnumeros.html")

def EvaluarNumero(request):
    if ('cajanum' in request.POST):
        #Hacemos cosas
        numero = int(request.POST["cajanum"])
        tipo = "Un texto que quiero dibujar en la pagina"
        if (numero % 2 == 0):
            tipo = "PAR"
        else:
            tipo = "IMPAR"
        informacion = {
            "resultado": tipo,
            "datonumero": numero
        }
        return render(request, "paginas/parimpar.html", informacion)
    else:
        return render(request, "paginas/parimpar.html")
