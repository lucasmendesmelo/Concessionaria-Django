from django.urls import path
from . import views


urlpatterns = [
    path('', views.lista_veiculos, name='lista_veiculos'),
    path('filtrar/', views.filtrar_veiculos, name='filtrar_veiculos'),
    path('sobre/', views.sobre, name='sobre')
    
]

