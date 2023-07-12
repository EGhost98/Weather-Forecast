from django.test import TestCase
from Forecast.forms import WeatherForecastForm

class TestForms(TestCase):
    def test_valid_form(self):
        form_data = {
            'latitude': 35.6895,
            'longitude': 139.6917,
            'detail': 'current'
        }
        form = WeatherForecastForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_form(self):
        form_data = {
            'latitude': 100,
            'longitude': 200,
            'detail': 'invalid_choice'
        }
        form = WeatherForecastForm(data=form_data)
        self.assertFalse(form.is_valid())
        # print(form.errors)
        self.assertEqual(len(form.errors), 3)
        self.assertEqual(form.errors['latitude'], ['Latitude must be between -90 and 90.'])
        self.assertEqual(form.errors['longitude'], ['Longitude must be between -180 and 180.'])
