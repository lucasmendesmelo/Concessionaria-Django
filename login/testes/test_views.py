from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.test import Client

class TesteLoginView(TestCase):
    def setUp(self):
        self.cliente = Client()
        self.nome_de_usuario = 'admin'
        self.senha = '123'
        self.usuario = User.objects.create_user(username=self.nome_de_usuario, password=self.senha)

    def test_login_com_credenciais_validas(self):
        resposta = self.cliente.post(reverse('login_view'), {'username': self.nome_de_usuario, 'password': self.senha})
        self.assertEqual(resposta.status_code, 302)  

    def test_login_com_credenciais_invalidas(self):
        resposta = self.cliente.post(reverse('login_view'), {'username': 'usuario_inexistente', 'password': 'senha_incorreta'})
        self.assertEqual(resposta.status_code, 200) 
        self.assertContains(resposta, 'Credenciais inválidas.') 

    def test_login_com_requisicao_get(self):
        resposta = self.cliente.get(reverse('login_view'))
        self.assertEqual(resposta.status_code, 200)  

