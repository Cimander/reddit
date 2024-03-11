from django.urls import path
from .views import PrintValueView, WeatherAPIView

urlpatterns = [
    path('pars/', PrintValueView.as_view(), name='parser'),
    path('weather/', WeatherAPIView.as_view(), name='weather'),
]