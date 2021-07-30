from typing import Counter
from django.http.response import JsonResponse
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, localtime, strftime
from django.utils.crypto import get_random_string
# Create your views here.

def index(request):
    return HttpResponse("esto es el random word!")

def random(request):
    counter = request.session.get('counter',0)
    #if 'counter' no existe en la session:
    if 'counter' not in request.session:
        request.session['counter'] = 0
    
    if counter >= 10:
        
        context = {'randomword':'Let me rest -.-'}
    else:
        request.session['counter']  +=1
        context = {'randomword':get_random_string(length=14),
                
        
        }
    
    return render(request,"random.html",context)

def generate(request):
    context = {'randomword':get_random_string(length=14)}
    return render(request,"random.html",context)

def login(request,name):
    
    request.session['name'] = name

    return redirect('/random_word/random')

def reset(request):

    request.session['counter'] = 0

    return redirect('/random_word/random')

def logout(request):
    counter = 0
    del request.session['name']
    
    
    return redirect('/random_word/random')