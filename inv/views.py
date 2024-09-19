from django.shortcuts import render
from django.views import generic #Esto es para que django importe views de la app inv 
#que es generic ? https://docs.djangoproject.com/en/3.1/topics/class-based-views/generic views/


# Create your views here.

#Esto es para que solo los usuarios logeados puedan acceder a la vista
from django.contrib.auth.mixins import LoginRequiredMixin 

from .models import Categoria  #El . es para importar el modelo de la app inv

class CategoriaView(LoginRequiredMixin, generic.ListView):
    model = Categoria
    template_name = 'inv/categoria_list.html'
    context_object_name = 'obj'
    login_url = 'bases:login'
