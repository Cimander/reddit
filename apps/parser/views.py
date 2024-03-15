<<<<<<< HEAD
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ValueSerializer
import requests
from bs4 import BeautifulSoup as BS
from pyowm import OWM


a = "table-responsive"
r = requests.get("https://www.nbkr.kg/index1.jsp?item=1562&lang=RUS")
soup = BS(r.text, 'html.parser')


# Извлекаем заголовки



class PrintValueView(APIView):
    def get(self, request, *args, **kwargs):
        valut = soup.find_all('td', class_='stat-left')
        price = soup.find_all('td', class_='stat-right')
        price = price[::2]

        list_1 = []
        list_2 = []
        for i in valut:
            list_1.append(i.text)
        for i in price:
            list_2.append(i.text)

        merged = [f'{x} = {y}' for x, y in zip(list_1, list_2)]
        
        serialized_values = ValueSerializer(merged, many=True)
        return Response(serialized_values.data)



owm = OWM('28c8e715bdb5d5bb438b2d1051508faa')
mgr = owm.weather_manager()

class WeatherAPIView(APIView):
    def get(self, request):
        location = request.GET.get('location', 'London,GB')
        observation = mgr.weather_at_place(location)
        w = observation.weather
        data = {
            "status": w.detailed_status,
            "wind": w.wind(),
            "humidity": w.humidity,
            "temperature": w.temperature('celsius'),
            "rain": w.rain,
            "heat_index": w.heat_index,
            "clouds": w.clouds,
        }
        return Response(data)
=======
from django.shortcuts import render

# Create your views here.
>>>>>>> origin/main
