from django.urls import path
from .views import  CustomUserRetrieveUpdateDestroy, RegisterView

urlpatterns = [

    path('register/', RegisterView.as_view(), name='user-list-create'),
    path('<int:pk>/', CustomUserRetrieveUpdateDestroy.as_view(), name='user-detail'),
]