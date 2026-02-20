from django.shortcuts import render
import math

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
    
def Collatz(request):
    if ('cajanumero' in request.POST):
        #Tenemos datos
        #Creamos una lista de numeros
        listanumeros = []
        #Leemos el numero de la caja
        numero = int(request.POST["cajanumero"])
        while (numero != 1):
            if (numero % 2 == 0):
                numero = numero / 2
                numero = numero * 3 + 1
            numero = math.trunc(numero)
            listanumeros.append(numero)
        informacion = {
            "listanumeros": listanumeros
        }
        #Devolvemos la informacion
        return render(request, "paginas/collatz.html", informacion)
    else:
        #sin datos
        return render(request, "paginas/collatz.html")
    
def TablaMultiplicar(request):
    if ('cajanumero' in request.POST):
        #Aqui recibimos datos
        numero = int(request.POST['cajanumero'])
        listaDatos = []
        for i in range(1, 11):
            operacion = f"{numero} * {i}" #5 * 1
            resultado = numero * i
            listaDatos.append(
                {
                    "operacion": operacion,
                    "resultado": resultado
                }
            )
        informacion = {
            "listadatos":listaDatos
        }
        return render(request, "paginas/tabla.html", informacion)
    else:
        return render(request, "paginas/tabla.html")

def deportes(request):
    listaDeportes = ["Futbol", "Petanca", "Curling", "Dardos", "Parchis", "Rana"]
    if ('selectdeporte' in request.POST):
        deporte = request.POST["selectdeporte"]
        informacion = {
            "listadeportes": listaDeportes,
            "deporte": deporte
        }
        return render(request, "paginas/deportes.html", informacion)
    else:
        informacion = {
            "listadeportes": listaDeportes
        }
        return render(request, "paginas/deportes.html", informacion)

def colores(request):
    listaColores = [
        {
            "nombrecolor": "Rojo",
            "valor": "red"
        },
        {
            "nombrecolor": "Amarillo",
            "valor": "yellow"
        },
        {
            "nombrecolor": "Verde",
            "valor": "lightgreen"
        },
        {
            "nombrecolor": "Azul",
            "valor": "lightblue"
        }
    ]
    if ('selectcolores' in request.POST):
        colorSeleccionado = request.POST["selectcolores"]
        informacion = {
            "listacolores": listaColores,
            "color": colorSeleccionado
        }
        return render(request, "paginas/colores.html", informacion)
    else:
        informacion = {
            "listacolores": listaColores
        }
        return render(request, "paginas/colores.html", informacion)

def comics(request):
    listacomics = [
        {
            "index": 0,
            "titulo": "Spiderman",
            "imagen": "https://elcoleccionistacomics.com/60266-medium_default/spiderman-de-todd-mcfarlane-vol1-de-6.jpg"
        },
        {
            "index": 1,
            "titulo": "Spawn",
            "imagen": "https://m.media-amazon.com/images/I/91hZO1pjAoL._AC_UF1000,1000_QL80_.jpg"
        },
        {
            "index": 2,
            "titulo": "Wolverine",
            "imagen": "https://www.kamekame.es/53918-large_default/marvel-omnibus-dinastia-de-x-potencias-de-x-comic.jpg"
        },
        {
            "index": 3,
            "titulo": "Wolverine",
            "imagen": "https://www.kamekame.es/53918-large_default/marvel-omnibus-dinastia-de-x-potencias-de-x-comic.jpg"
        },
        {
            "index": 4,
            "titulo": "Asterix y Obelix",
            "imagen": "https://comicsbarcelona.com/wp-content/uploads/2015/11/127913-Asterix-2.-La-Hoz-de-Oro.jpg"
        } 
               
              
    ]
    if ('selectcomic' in request.POST):
        indice = int(request.POST["selectcomic"])
        comic = listacomics[indice]
        informacion = {
            "listacomics": listacomics,
            "comic": comic
        }
        return render(request, "paginas/comics.html", informacion)
    else:
        informacion = {
            "listacomics": listacomics
        }
        return render(request, "paginas/comics.html", informacion)

