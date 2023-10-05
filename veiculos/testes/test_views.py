from django.test import TestCase
from django.urls import reverse
from veiculos.models import Veiculo


class VeiculoViewsTestCase(TestCase):
    def setUp(self):
        
        self.veiculo = Veiculo.objects.create(
            modelo="volvo s60",
            marca="volvo",
            tipo="carro",

        )

    def test_lista_veiculos(self):
        response = self.client.get(reverse('lista_veiculos'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lista_veiculos.html')
        self.assertIn(self.veiculo, response.context['veiculos'])

    def test_filtrar_veiculos(self):
        response = self.client.get(reverse('filtrar_veiculos'), {'tipo': 'todos', 'termo': 'Exemplo'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lista_veiculos.html')
        self.assertIn(self.veiculo, response.context['veiculos'])

        response = self.client.get(reverse('filtrar_veiculos'), {'tipo': 'sedan', 'termo': 'Exemplo'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lista_veiculos.html')
        self.assertIn(self.veiculo, response.context['veiculos'])

    def test_filtrar_veiculos_sem_resultados(self):
        response = self.client.get(reverse('filtrar_veiculos'), {'tipo': 'todos', 'termo': 'NaoExiste'})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'lista_veiculos.html')
        self.assertNotIn(self.veiculo, response.context['veiculos'])
