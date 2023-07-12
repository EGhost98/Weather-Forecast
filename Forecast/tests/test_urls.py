from django.test import SimpleTestCase
from django.urls import reverse, resolve
from Forecast import views

class TestUrls(SimpleTestCase):
    def test_weatherapi_list_url_resolves(self):
        url = reverse('weather-list')
        self.assertEqual(resolve(url).func.cls, views.weatherapi)

    def test_index_url_resolves(self):
        url = reverse('index')
        self.assertEqual(resolve(url).func, views.index)
