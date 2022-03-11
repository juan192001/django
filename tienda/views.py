from django.http import HttpResponse
from django.shortcuts import render



def tienda(request):
    return HttpResponse("Tienda")

def inicio(request):
    return HttpResponse("Inicio")