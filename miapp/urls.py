
from django.urls import path
from . import views

urlpatterns = [
 
  
    path("contacto/",views.contacto, name="contacto"),
    path("turismo/",views.turismo, name="turismo"),
    path("iserp/",views.iserp, name="iserp"),
    path("isers/",views.isers, name="isers"),
    path("iseer/",views.iseer, name="iseer"),
    path("recorrido/",views.recorrido, name="recorrido")
]