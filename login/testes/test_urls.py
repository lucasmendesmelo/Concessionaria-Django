from django.test import SimpleTestCase
from django.urls import reverse, resolve
from ..views import login_view


class TestUrls(SimpleTestCase):
    def test_se_url_login_esta_mapeando_funcao_view(self):
        url = reverse('login_view')
        self.assertEqual(resolve(url).func, login_view)
        
