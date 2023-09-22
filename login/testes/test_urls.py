from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import login_view


class TestUrls(SimpleTestCase):
    def test_se_url_login_esta_mapeando_funcao_view(self):
        url = reverse('login_view')
        self.assertEqual(resolve(url).func, login_view)
        
#  O método test_se_url_login_esta_mapeando_funcao_view verifica se a URL /login/ 
# está mapeada para a função de visualização login_view