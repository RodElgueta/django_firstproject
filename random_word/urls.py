from django.urls import path     
from . import views

urlpatterns = [
    path('', views.index),
    path('random',views.random),
    path('login/<name>',views.login),
    path('logout/<name>',views.logout),
    path('reset',views.reset)
    ]