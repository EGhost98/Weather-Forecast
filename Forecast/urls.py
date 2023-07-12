from django.urls import path, include
from rest_framework.routers import DefaultRouter
from django.conf.urls import handler404
from . import views

weather_router = DefaultRouter()
weather_router.register(r'weather', views.weatherapi, basename='weather')

urlpatterns = [
    path('api/', include(weather_router.urls)),
    path('',views.index, name='index'),
]

handler404 = views.error_404