#Rutas para mi servidor https://paco
from django.urls import path
#Los metodos que tenemos en views.py
from aplicacion import views
#Creamos las rutas
#http://127.0.0.1:8000/aplicacion
#http://127.0.0.1:8000/aplicacion/prueba
urlpatterns = [
     path('', views.index, name="index"),
     path('prueba/', views.prueba, name="prueba")
]
