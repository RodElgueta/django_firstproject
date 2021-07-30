from django.urls import path     
from . import views

# siempre tratar de dejar los paths mas especificos arriba
urlpatterns = [
    path('repyt/<video>',views.videos),
    path('', views.root),
    path('dos/', views.func2),	  
    path('blogs/',views.index),
    path('blogs/new',views.new),
    path('blogs/create',views.create),
    path('blogs/<int:num>',views.show),
    path('blogs/<int:num>/edit',views.edit),
    path('blogs/<int:num>/delete',views.destroy),
    path('blogs/json',views.json),
    path('index/',views.index2),
    path('imgs/',views.img),
    path('try/<name>',views.template_try),
    path('time',views.time),
    path('login/<name>',views.login)
    

]
