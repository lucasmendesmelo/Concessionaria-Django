from django.shortcuts import render, redirect
from .models import Veiculo
from django.db.models import Q
from django.contrib.auth import authenticate, login




def lista_veiculos(request):
    veiculos = Veiculo.objects.all()
    
    return render(request, 'lista_veiculos.html', {'veiculos': veiculos})



def filtrar_veiculos(request):
    tipo = request.GET.get('tipo')
    termo = request.GET.get('termo')  # Renomeie o campo para 'termo'

    # Filtrar veículos com base no tipo, modelo e marca
    if tipo == 'todos':
        veiculos = Veiculo.objects.filter(Q(modelo__icontains=termo) | Q(marca__icontains=termo))
    else:
        veiculos = Veiculo.objects.filter(Q(tipo=tipo) & (Q(modelo__icontains=termo) | Q(marca__icontains=termo)))

    # Manter a seleção de filtro
    tipo_selecionado = tipo if tipo != 'todos' else ''

    return render(request, 'lista_veiculos.html', {
        'veiculos': veiculos,
        'tipo_selecionado': tipo_selecionado,
        'termo_inserido': termo,  # Passe o valor do termo inserido para a página HTML
    })


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('admin:index')  # Redirecionar para o painel de administração
        else:
            # Tratamento de erro caso as credenciais estejam incorretas
            error_message = 'Credenciais inválidas. Tente novamente.'
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')