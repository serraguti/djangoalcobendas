#Rutas para mi servidor https://paco
from django.urls import path
#Los metodos que tenemos en views.py
from aplicacion import views
#Creamos las rutas
#http://127.0.0.1:8000/aplicacion
#http://127.0.0.1:8000/aplicacion/prueba
#http://127.0.0.1:8000/aplicacion/peliculas
urlpatterns = [
     path('', views.index, name="index"),
     path('prueba/', views.prueba, name="prueba"),
     path("peliculas/", views.peliculas, name="peliculas"),
]
