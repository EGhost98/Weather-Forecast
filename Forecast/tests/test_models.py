import os
import json
from django.test import TestCase
from django.core.exceptions import ValidationError
from Forecast.models import WeatherForecast

class WeatherForecastModelTest(TestCase):
    def setUp(self):
        super().setUp()
        test_data_path = os.path.join(os.path.dirname(__file__), 'test_data.json')
        with open(test_data_path) as file:
            self.json_data = json.load(file)

    def test_valid_latitude_longitude(self):
        weather_forecast = WeatherForecast(
            latitude=29.8646495,
            longitude=77.8938784,
            detailing_type='current',
            weather_data=self.json_data,
            timestamp=None
        )

        weather_forecast.full_clean()
        weather_forecast.save()
        saved_weather_forecast = WeatherForecast.objects.get(pk=weather_forecast.pk)
        self.assertEqual(weather_forecast, saved_weather_forecast)

    def test_invalid_latitude_longitude(self):
        weather_forecast = WeatherForecast(
            latitude=100,
            longitude=200,
            detailing_type='current',
            weather_data=self.json_data,
            timestamp=None
        )

        with self.assertRaises(ValidationError):
            weather_forecast.full_clean()

    def test_unique_together_constraint(self):
        weather_forecast1 = WeatherForecast(
            latitude=35.6895,
            longitude=139.6917,
            detailing_type='current',
            weather_data=self.json_data,
            timestamp=None
        )
        weather_forecast1.save()

        weather_forecast2 = WeatherForecast(
            latitude=35.6895,
            longitude=139.6917,
            detailing_type='current',
            weather_data=self.json_data,
            timestamp=None
        )

        with self.assertRaises(ValidationError):
            weather_forecast2.full_clean()
