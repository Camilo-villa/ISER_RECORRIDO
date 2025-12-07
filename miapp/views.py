from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def contacto (request):
    return render(request, 'contacto.html')
def turismo (request):
    return render(request, 'turismo.html')
def iserp (request):
    return render(request, 'iser.html')
def isers (request):
    return render(request, 'iser2.html')
def iseer (request):
    return render(request, 'iseer.html')
def recorrido (request):
    return render(request, 'recorrido.html')