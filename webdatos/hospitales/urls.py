from hospitales import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path("departamentos/", views.tabladepartamentos, name="departamentos"),
    path("insertdept/", views.insertarDepartamento, name="insertdept"),
    path("updatedept/", views.updateDepartamento, name="updatedept"),
    path("buscarform/", views.buscarDepartamentoForm, name="buscarform"),
    path("buscarget/", views.buscarDepartamentoGet, name="buscarget"),
    path("delete/", views.delete, name="delete"),
]
