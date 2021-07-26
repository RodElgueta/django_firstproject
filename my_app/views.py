# Create your views here.
from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, redirect


def index(request):
    return HttpResponse("placeholder para luego mostrar una lista de todos los blogs")

def func2(request):
    return HttpResponse("hello im skynet")

def root(request):
    return redirect("/blogs")

def new(request):
    return HttpResponse("placeholder para mostrar un nuevo formulario para crear un nuevo blog")

def create(request):
    return redirect("/")

def show(request,num):
    return HttpResponse(f"placeholder para mostrar el blog numero {num}")

def edit(request,num):
    return HttpResponse(f"placeholder para editar el blog {num}")

def destroy(resquest,num):
    return redirect("/blogs")

def json(request):
    return JsonResponse({
        'nombre':"rodrigo",
        'edad':33,
        "voz":'44khz'


    })