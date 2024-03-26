from django.urls import path
from .views import PrintValueView, WeatherAPIView, WeatherListAPIView

urlpatterns = [
    path('pars/', PrintValueView.as_view(), name='parser'),
    path('create/', WeatherAPIView.as_view(), name='weather'),
    path('weather/', WeatherListAPIView.as_view(), name='weather'),
]