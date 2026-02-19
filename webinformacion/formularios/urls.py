from django.urls import path
from formularios import views

urlpatterns = [
    path('', views.index, name="index")
]
