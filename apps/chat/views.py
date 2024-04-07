from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from apps.user.permissions import IsAdminPermission
from .models import Message, Group
from .serializers import MessageSerializer, GroupSerializer, GroupListSerializer
from apps.user.serializer import UserSerializer
from ..user.models import User


class GroupListCreate(generics.ListCreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]

class GroupRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny]
    lookup_field = 'pk'

class GroupMembersList(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        group_id = self.kwargs['pk']
        return Group.objects.get(id=group_id).members.all()

class GroupDeleteView(generics.DestroyAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [AllowAny, IsAdminPermission]

    def delete(self, request, *args, **kwargs):
        group = self.get_object()
        group.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class MessageListCreateView(generics.ListCreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [AllowAny]

    def perform_create(self, serializer):

        group_pk = self.kwargs.get('pk')  # Получаем pk из URL
        group = Group.objects.get(id=group_pk)  # предположим, что у вас есть id группы

        member_ids = group.members.values_list('id', flat=True)
        members = group.members.all()



        if serializer.validated_data['user'].id in member_ids:
            serializer.save(group_id=group_pk)
class MessageRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]

class GroupRetrieveView(generics.RetrieveAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupListSerializer
    lookup_field = 'pk'
    permission_classes = [AllowAny]
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)