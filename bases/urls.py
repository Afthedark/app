#Este archivo urls se crea manualmente en la app bases para que django reconozca las urls de bases

from django.urls import path
from django.contrib.auth import views as auth_views  #Para que django reconozca las urls de django.contrib.auth.views

from bases.views import Home # Esto es para que django importe views de la app bases despues se llama a la clase Home de views

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('login/', auth_views.LoginView.as_view(template_name='bases/login.html'), 
         name='login'),
    path('logout/', 
         auth_views.LogoutView.as_view(template_name='bases/login.html'), 
         name='logout'),
]