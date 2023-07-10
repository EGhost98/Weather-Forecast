from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

weather_router = DefaultRouter()
weather_router.register(r'weather', views.weatherapi, basename='weather')

urlpatterns = [
    path('api/', include(weather_router.urls)),
    path('index',views.index, name='index'),
]
