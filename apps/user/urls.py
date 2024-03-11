from django.urls import path
from django.contrib.auth import views as auth_views
from .views import RegisterView, LoginAPIView
#from .Telegram import main

urlpatterns = [
    path('registr/', RegisterView.as_view(), name='registration'),
    path('login/', LoginAPIView.as_view(), name='login'),
    #path('send_message/', main, name='send_telegram_message'),
]