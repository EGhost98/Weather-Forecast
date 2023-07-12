from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from rest_framework import status
from django.shortcuts import render
import requests
from django.conf import settings
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import WeatherForecast
from django.utils import timezone
from .api_url import get_api_url
from .forms import WeatherForecastForm
import json

def index(request):
    context = {}
    form = WeatherForecastForm()
    context['form'] = form
    if request.method == 'GET':
        form = WeatherForecastForm(request.GET)
        if form.is_valid():
            lat = form.cleaned_data['latitude']
            lon = form.cleaned_data['longitude']
            detailing_type = form.cleaned_data['detail']
            host_url = request.build_absolute_uri('/')
            api_endpoint_url = f'{host_url}/api/weather?lat={lat}&lon={lon}&detail={detailing_type}'
            Weather_data = requests.get(api_endpoint_url).json()
            if int(Weather_data['cod']) != 200:
                context['errors'] = 'Api Key Dosen\'t have Required Authentication (Limited Access).'
                Weather_data = None
            context['Weather_Data'] = Weather_data
            context['raw_json'] = json.dumps(Weather_data)
            context['detail'] = detailing_type
            return render(request, 'forecast/index.html', context)
        else:
            context['errors'] = form.errors
    return render(request, 'forecast/index.html', context)


class weatherapi(ViewSet):
    permission_classes = [AllowAny]
    
    def list(self, request):
        lat = request.query_params.get('lat')
        lon = request.query_params.get('lon')
        detail = request.query_params.get('detail')
        weather_forecast = WeatherForecast.objects.filter(latitude=lat, longitude=lon, detailing_type=detail).first()
        if weather_forecast and weatherapi.is_data_up_to_date(weather_forecast):
            return Response(weather_forecast.weather_data)
        api_key = settings.OPENWEATHERMAP_API_KEY
        api_url = get_api_url(detail,api_key,lat,lon)
        if not api_url:
            return Response({'detail' : 'Invalid Parameters!'},status=status.HTTP_400_BAD_REQUEST)
        response = requests.get(api_url)
        weather_data = response.json()
        if weather_forecast:
            weather_forecast.weather_data = weather_data
            if int(weather_data['cod']) == 200:
                weather_forecast.save()
        else:
            WeatherForecast.objects.create(latitude=lat, longitude=lon, detailing_type=detail, weather_data=weather_data)
            
        return Response(weather_data)
    
    def is_data_up_to_date(weather_forecast):
        delta = timezone.now() - weather_forecast.timestamp
        return delta.total_seconds() <= int(settings.LOCAL_DATA_EXPIRATION)