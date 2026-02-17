from django.urls import path
from practica import views

urlpatterns = [
    path("martes/", views.index, name="index")
]