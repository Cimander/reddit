from rest_framework import viewsets, permissions, status, generics
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Post, Comment, Like, Cart, Category
from .serializers import (
    PostSerializer,
    CommentSerializer,
    LikeSerializer,
    PostCreateSerializer,

    CategorySerializer,
    CartUpdateSerializer,
    CartSerializer)


class PostCreateAPIView(generics.CreateAPIView):

    serializer_class = PostCreateSerializer
    permission_classes = [permissions.AllowAny]

class LikeCreateAPIView(generics.CreateAPIView):

    serializer_class = LikeSerializer
    permission_classes = [permissions.AllowAny]
class PostListAPIView(generics.ListAPIView):
    permission_classes = [permissions.AllowAny]
    serializer_class = PostSerializer
    queryset = Post.objects.all()
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ['title']


class CommentViewSet(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [permissions.AllowAny]








class PostUpdateAPIView(generics.RetrieveUpdateAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    lookup_field = 'pk'


class PostDeleteAPIView(generics.DestroyAPIView):
    queryset = Post.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = PostSerializer
    lookup_field = 'pk'

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class CartAPIView(APIView):
    permission_classes = [permissions.AllowAny]


    def post(self, request):  # Обратите внимание на добавленный параметр self
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartUpdateAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def put(self, request, id):
        snippet = Cart.objects.get(user_id=id)
        serializer = CartUpdateSerializer(snippet, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CartResetAPIView(APIView):
    permission_classes = [permissions.AllowAny]

    def put(self, request, id):
        snippet = Cart.objects.get(user_id=id)
        snippet.save()
        return Response({"response": 'reset was successfull'}, status=status.HTTP_200_OK)