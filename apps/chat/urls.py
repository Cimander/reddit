
from django.urls import path
from .views import ChatListCreateAPIView, MessageListCreateAPIView, UserFilterListAPIView

urlpatterns = [
    path('chats/', ChatListCreateAPIView.as_view(), name='chat-list-create'),
    path('chats/<int:chat_id>/messages/', MessageListCreateAPIView.as_view(), name='message-list-create'),
    path('filter/user/', UserFilterListAPIView.as_view(), name='user-filter'),
]