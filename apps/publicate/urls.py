from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostListAPIView,
    CommentViewSet,
    LikeCreateAPIView,
    PostCreateAPIView,
    PostRetrieveUpdateDestroy,
    PostListCopy,
    #CartAPIView,
    #CartRetrieveUpdateDestroy,
    CategoryViewSet)



urlpatterns = [
    path('', PostListAPIView.as_view(), name='list-post'),
    path('copy/', PostListCopy.as_view(), name='list-post'),

    path('create/', PostCreateAPIView.as_view(), name='post-create'),
    path('redact/<int:pk>/', PostRetrieveUpdateDestroy.as_view(), name='post-redact'),
    path('comment/', CommentViewSet.as_view(), name='comment'),
    path('like/', LikeCreateAPIView.as_view(), name='like'),
    path('category/', CategoryViewSet.as_view({'get': 'list'}), name='category'),



    #path('cart/', CartAPIView.as_view(), name='cart'),
    #path('cart/<int:pk>/', CartRetrieveUpdateDestroy.as_view(), name='cart-update'),

]