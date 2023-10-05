from django.shortcuts import render, redirect
from .models import Veiculo
from django.db.models import Q





def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    
    return render(request, 'lista_veiculos.html', {'veiculos': veiculos})



def filtrar_veiculos(request):
    tipo = request.GET.get('tipo')
    termo = request.GET.get('termo')  

    
    if tipo == 'todos':
        veiculos = Veiculo.objects.filter(Q(modelo__icontains=termo) | Q(marca__icontains=termo))
    else:
        veiculos = Veiculo.objects.filter(Q(tipo=tipo) & (Q(modelo__icontains=termo) | Q(marca__icontains=termo)))

    
    tipo_selecionado = tipo if tipo != 'todos' else ''

    return render(request, 'lista_veiculos.html', {
        'veiculos': veiculos,
        'tipo_selecionado': tipo_selecionado,
        'termo_inserido': termo, 
    })


