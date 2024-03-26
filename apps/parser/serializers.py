from rest_framework import serializers
from .models import City
class ValueSerializer(serializers.Serializer):
    value = serializers.CharField(source='*')

class WeatherSerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = '__all__'

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['content']