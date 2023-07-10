from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
import requests
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import WeatherForecast
from django.utils import timezone
from .api_url import get_api_url

class weatherapi(ViewSet):
    permission_classes = [AllowAny]
    
    def list(self, request):
        lat = request.query_params.get('lat')
        lon = request.query_params.get('lon')
        detail = request.query_params.get('detail')
        weather_forecast = WeatherForecast.objects.filter(latitude=lat, longitude=lon, detailing_type=detail).first()
        if weather_forecast and weatherapi.is_data_up_to_date(weather_forecast):
            return weather_forecast.weather_data
        api_key = settings.OPENWEATHERMAP_API_KEY
        api_url = get_api_url(detail,api_key,lat,lon)
        if not api_url:
            return Response({'detail' : 'Invalid Parameters!'},status=status.HTTP_400_BAD_REQUEST)
        response = requests.get(api_url)
        weather_data = response.json()
        if weather_forecast:
            weather_forecast.weather_data = weather_data
            weather_forecast.save()
        else:
            WeatherForecast.objects.create(latitude=lat, longitude=lon, detailing_type=detail, weather_data=weather_data)
            
        return Response(weather_data)
    
    def is_data_up_to_date(weather_forecast):
        delta = timezone.now() - weather_forecast.timestamp
        return delta.total_seconds() <= settings.LOCAL_DATA_EXPIRATION

# @csrf_exempt
# def index(request):
#     if request.method == 'GET':
#         lat = request.GET.get('lat')
#         lon = request.GET.get('lon')
#         detailing_type = request.GET.get('detailing_type')

#         weather_data = get_weather_data(lat, lon, detailing_type)

#         return JsonResponse({'weather_data': weather_data})

#     return JsonResponse({'error': 'Invalid request method'})
