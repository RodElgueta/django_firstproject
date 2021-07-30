# Create your views here.
from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, localtime, strftime


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

def index2(request):
    return render(request, "index.html")

def template_try(request,name):
    
    context = {
        "myname":name,
        "fav_color":"skyblue",
        "pets":["lixa","canela","tortu","canito"],
        "petsimg":["https://www.hola.com/imagenes/estar-bien/20201218181375/dejar-solo-gato-en-casa/0-902-780/gato-solo-casa-t.jpg",
                "https://perro-salchicha.com/wp-content/uploads/2020/11/perro-salchicha-pelo-corto.jpg",
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTx-113zzmbT6fG1sW6Re5oLlO2mJF-iokfNg&usqp=CAU",
                "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSaPKBFxeAaAU6z4fVJKlxA4lmDT0gg99hdNQ&usqp=CAU"]
    }
    return render(request,"index.html",context)

def videos(request, video):
    context2 = {
        'video' : video,

    }
    return render(request, "videos.html", context2)

def img(request):
    context3 = {
        'petsdict' : {"lixa":"https://www.hola.com/imagenes/estar-bien/20201218181375/dejar-solo-gato-en-casa/0-902-780/gato-solo-casa-t.jpg",
        "canela":"https://perro-salchicha.com/wp-content/uploads/2020/11/perro-salchicha-pelo-corto.jpg",
        "tortu":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTx-113zzmbT6fG1sW6Re5oLlO2mJF-iokfNg&usqp=CAU",
        "canito":"https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSaPKBFxeAaAU6z4fVJKlxA4lmDT0gg99hdNQ&usqp=CAU"}}
        
                
    return render(request,"img.html",context3)

def time(request):
    context = {
        "time":strftime("%Y-%m-%d %H:%M %p ", localtime()),
        "diftime":strftime("%z"),
        "gmtime":strftime("%Y-%m-%d %H:%M %p ", gmtime()),
    }
    return render(request,'time.html',context)

def login(request,name):
    request.session['name'] = name

    return redirect('/time')

def salir(request):
    del request.session['name']
    request.session['counter'] = 100
    return