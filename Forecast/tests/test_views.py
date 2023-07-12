import os
import json
import time
from django.utils import timezone
from django.test import TestCase, RequestFactory
from Forecast.views import index, weatherapi
from Forecast.forms import WeatherForecastForm
from Forecast.models import WeatherForecast
from django.urls import reverse
from rest_framework.test import APIRequestFactory
from unittest.mock import patch
from django.conf import settings

class IndexViewTest(TestCase):
    def test_index_view_get(self):
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forecast/index.html')

    @patch('Forecast.views.requests.get')
    def test_index_view_post_valid_form(self, mock_get):
        url = reverse('index')
        form_data = {
            'latitude': 35.6895,
            'longitude': 139.6917,
            'detail': 'current'
        }
        test_data_path = os.path.join(os.path.dirname(__file__), 'test_data.json')
        with open(test_data_path) as file:
            valid_response_data = json.load(file)
        mock_response = mock_get.return_value
        mock_response.json.return_value = valid_response_data
        response = self.client.post(url, form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forecast/index.html')
        self.assertIn('Weather_Data', response.context)
        self.assertIn('detail', response.context)
        self.assertIn('raw_json', response.context)

    @patch('Forecast.views.requests.get')
    def test_index_view_post_invalid_form(self, mock_get):
        url = reverse('index')
        form_data = {
            'latitude': 100,
            'longitude': 200,
            'detail': 'invalid_choice'
        }
        response = self.client.post(url, form_data)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'forecast/index.html')
        self.assertIn('errors', response.context)


class WeatherAPIViewTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    @patch('Forecast.views.requests.get')
    def test_list_valid_request(self, mock_get):
        lat = 35.6895
        lon = 139.6917
        detail = 'current'
        url = reverse('weather-list') 
        request = self.factory.get(url, {'lat': lat, 'lon': lon, 'detail': detail})
        test_data_path = os.path.join(os.path.dirname(__file__), 'test_data.json')
        with open(test_data_path) as file:
            valid_response_data = json.load(file)
        mock_response = mock_get.return_value
        mock_response.json.return_value = valid_response_data
        response = weatherapi.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['cod'], 200)

    @patch('Forecast.views.requests.get')
    def test_list_invalid_request(self, mock_get):
        lat = 35.6895
        lon = 139.6917
        detail = 'invalid_detail'
        url = reverse('weather-list') 
        request = self.factory.get(url, {'lat': lat, 'lon': lon, 'detail': detail})
        response = weatherapi.as_view({'get': 'list'})(request)
        self.assertEqual(response.status_code, 400)
        self.assertEqual(response.data['detail'], 'Invalid Parameters!')


    def test_is_data_up_to_date(self):
        weather_forecast = WeatherForecast.objects.create(
            latitude=35.6895,
            longitude=139.6917,
            detailing_type='current',
            weather_data={},
        )
        time.sleep(3)
        result = weatherapi.is_data_up_to_date(weather_forecast)
        delta = timezone.now() - weather_forecast.timestamp
        expiration_seconds = int(settings.LOCAL_DATA_EXPIRATION)
        self.assertEqual(delta.total_seconds() <= expiration_seconds, result)
