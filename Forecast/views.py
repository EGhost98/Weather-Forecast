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
    if request.method == 'POST':
        form = WeatherForecastForm(request.POST)
        if form.is_valid():
            lat = form.cleaned_data['latitude']
            lon = form.cleaned_data['longitude']
            detailing_type = form.cleaned_data['detail']
            appid = form.cleaned_data['appid']
            host_url = request.build_absolute_uri('/')
            api_endpoint_url = f'{host_url}/api/weather?lat={lat}&lon={lon}&detail={detailing_type}&appid={appid}'
            Weather_data = requests.get(api_endpoint_url).json()
            context['raw_json'] = json.dumps(Weather_data)
            if int(Weather_data['cod']) == 401:
                context['errors'] = 'Invalid API Key, Dosen\'t have Required Authentication'
                Weather_data = None
            context['Weather_Data'] = Weather_data
            context['detail'] = detailing_type
            if appid:
                context['last_appid'] = appid
            if lat:
                form.fields['latitude'].widget.attrs['value'] = lat
            if lon:
                context['last_lon'] = lon
            if detailing_type:
                context['last_detail'] = detailing_type
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
        appid = request.query_params.get('appid')
        if not lat or not lon or not detail:
            return Response({'detail': 'Invalid Parameters'}, status=status.HTTP_400_BAD_REQUEST)
        weather_forecast = WeatherForecast.objects.filter(latitude=lat, longitude=lon, detailing_type=detail).first()
        if weather_forecast and weatherapi.is_data_up_to_date(weather_forecast):
            return Response(weather_forecast.weather_data)
        if appid:
            api_key = appid
        else:
            api_key = settings.OPENWEATHERMAP_API_KEY
        api_url = get_api_url(detail,api_key,lat,lon)
        if not api_url:
            return Response({'detail' : 'Invalid Parameters'},status=status.HTTP_400_BAD_REQUEST)
        response = requests.get(api_url)
        weather_data = response.json()
        if weather_forecast and int(weather_data['cod']) == 200:
                weather_forecast.weather_data = weather_data
                weather_forecast.save()
        elif int(weather_data['cod']) == 200:
            WeatherForecast.objects.create(latitude=lat, longitude=lon, detailing_type=detail, weather_data=weather_data)
        return Response(weather_data)
    
    def is_data_up_to_date(weather_forecast):
        delta = timezone.now() - weather_forecast.timestamp
        # print(weather_forecast.timestamp)
        # print(delta.total_seconds())
        return delta.total_seconds() <= int(settings.LOCAL_DATA_EXPIRATION)

def error_404(request,  *args, **kwargs):
    return render(request, '404.html', status=404)