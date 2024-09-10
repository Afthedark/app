# Modificamos viwes.py de la app bases para que django reconozca las urls de bases

from django.shortcuts import render

#Importando la clase LoginRequiredMixin para que solo los usuarios logeados puedan acceder a la vista
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.views import generic

# Create your views here.

class Home(LoginRequiredMixin, generic.TemplateView): # Dentro de la raiz del proyecto buscara la carpeta templates y luego la carpeta bases 
    template_name = 'bases/home.html'
    login_url = 'bases:login' # Si no esta logeados redirecciona al admin




