from hospitales import views
from django.urls import path

urlpatterns = [
    path('', views.index, name="index"),
    path("departamentos/", views.tabladepartamentos, name="departamentos"),
    path("insertdept/", views.insertarDepartamento, name="insertdept"),
    path("updatedept/", views.updateDepartamento, name="updatedept"),
]
