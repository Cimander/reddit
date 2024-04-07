from rest_framework import serializers
from .models import Message, Group

class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name', 'members']

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ['user',  'content', 'created_at']

comments = serializers.SerializerMethodField()

class GroupListSerializer(serializers.ModelSerializer):
    message = serializers.SerializerMethodField()
    class Meta:
        model = Group
        fields = "__all__"

    def get_message(self, obj):
        message = Message.objects.filter(group_id=obj.id)
        return MessageSerializer(message, many=True).data