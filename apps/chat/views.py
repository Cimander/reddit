from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from apps.user.serializer import UserSerializer
from .models import Chat, Message
from .serializers import ChatSerializer, MessageSerializer
from apps.user.models import User
class ChatListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = ChatSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Chat.objects.filter(user1=self.request.user) | Chat.objects.filter(user2=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user1=self.request.user)

class UserFilterListAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def get(self, request):
        if request.query_params.get('search'):
            objects = User.objects.filter(name__contains=request.query_params.get('search'))
        else:
            objects = User.objects.all()
        serializer = UserSerializer(objects, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)
class MessageListCreateAPIView(generics.ListCreateAPIView):
    serializer_class = MessageSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        chat_id = self.kwargs['chat_id']
        chat = Chat.objects.get(id=chat_id)
        if self.request.user == chat.user1 or self.request.user == chat.user2:
            return Message.objects.filter(chat=chat)

    def perform_create(self, serializer):
        chat_id = self.kwargs['chat_id']
        chat = Chat.objects.get(id=chat_id)
        if self.request.user == chat.user1 or self.request.user == chat.user2:
            serializer.save(sender=self.request.user, chat=chat)