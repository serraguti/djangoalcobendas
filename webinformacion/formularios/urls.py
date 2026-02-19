from django.urls import path
from formularios import views

urlpatterns = [
    path('', views.index, name="index"),
    path('ejemplo/', views.ejemplo, name="ejemplo"),
    path("saludo/", views.saludo, name="saludo"),
    path("sumar/", views.SumarNumeros, name="sumar"),
    path("parimpar/", views.EvaluarNumero, name="parimpar"),
    path("collatz/", views.Collatz, name="collatz"),
]
