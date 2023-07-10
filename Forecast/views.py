from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
import requests
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import WeatherForecast
from django.utils import timezone


class weatherapi(ViewSet):
    permission_classes = [AllowAny]

def list(self, request):
    lat = request.query_params.get('lat')
    long = request.query_prams.get('long')
    detail = request.query_params.get('')


@csrf_exempt
def weather_forecast(request):
    if request.method == 'GET':
        lat = request.GET.get('lat')
        lon = request.GET.get('lon')
        detailing_type = request.GET.get('detailing_type')

        weather_data = get_weather_data(lat, lon, detailing_type)

        return JsonResponse({'weather_data': weather_data})

    return JsonResponse({'error': 'Invalid request method'})


def get_weather_data(lat, lon, detailing_type):
    weather_forecast = WeatherForecast.objects.filter(latitude=lat, longitude=lon, detailing_type=detailing_type).first()

    if weather_forecast and is_data_up_to_date(weather_forecast):
        return weather_forecast.weather_data

    api_key = settings.OPENWEATHERMAP_API_KEY
    api_url = f'https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude=minutely,hourly&units=metric&appid={api_key}'

    response = requests.get(api_url)
    response_data = response.json()

    if 'daily' in response_data:
        weather_data = response_data['daily']
    elif 'hourly' in response_data:
        weather_data = response_data['hourly']
    else:
        weather_data = []

    if weather_forecast:
        weather_forecast.weather_data = weather_data
        weather_forecast.save()
    else:
        WeatherForecast.objects.create(latitude=lat, longitude=lon, detailing_type=detailing_type, weather_data=weather_data)

    return weather_data


def is_data_up_to_date(weather_forecast):
    delta = timezone.now() - weather_forecast.timestamp
    return delta.total_seconds() <= settings.LOCAL_DATA_EXPIRATION
