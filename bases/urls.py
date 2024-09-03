#Este archivo urls se crea manualmente en la app bases para que django reconozca las urls de bases

from django.urls import path

from bases.views import Home # Esto es para que django importe views de la app bases despues se llama a la clase Home de views

urlpatterns = [
    path('', Home.as_view(), name='home'), # 
]