from rest_framework import serializers

class ValueSerializer(serializers.Serializer):
    value = serializers.CharField(source='*')