
from django.urls import path
from .views import (
                    GroupListCreate,
                    GroupRetrieveUpdateDestroy,
                    GroupMembersList,
                    MessageListCreateView,
                    MessageRetrieveUpdateDestroyView,
                    GroupRetrieveView)

urlpatterns = [
    path('groups/', GroupListCreate.as_view(), name='group-list-create'),
    path('groups/look/<int:pk>/', GroupRetrieveView.as_view(), name='group-list'),
    path('groups/<int:pk>/', GroupRetrieveUpdateDestroy.as_view(), name='group-detail'),
    path('groups/<int:pk>/members/', GroupMembersList.as_view(), name='group-members-list'),
    path('messages/create/<int:pk>/', MessageListCreateView.as_view(), name='message-list-create'),
    path('messages/<int:pk>/', MessageRetrieveUpdateDestroyView.as_view(), name='message-detail'),
]