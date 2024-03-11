from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    PostListAPIView,
    CommentViewSet,
    LikeCreateAPIView,
    PostCreateAPIView,
    PostUpdateAPIView,
    PostFilterListAPIView,
    PostDeleteAPIView,
    CartAPIView,
    CartUpdateAPIView,
    CartResetAPIView)



urlpatterns = [
    path('', PostListAPIView.as_view(), name='list-post'),
    path('create/', PostCreateAPIView.as_view(), name='post-create'),
    path('update/', PostUpdateAPIView.as_view(), name='post-update'),
    path('<int:pk>/delete/', PostDeleteAPIView.as_view(), name='post-delete'),
    path('filter/', PostFilterListAPIView.as_view(), name='post-filter'),
    path('comment/', CommentViewSet.as_view(), name='comment'),
    path('like/', LikeCreateAPIView.as_view(), name='like'),


    path('cart/<int:id>/', CartAPIView.as_view(), name='cart'),
    path('cart/<int:id>/update/', CartUpdateAPIView.as_view(), name='cart-update'),
    path('cart/<int:id>/reset/', CartResetAPIView.as_view(), name='cart-reset'),
]