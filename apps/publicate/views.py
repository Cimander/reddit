from rest_framework import viewsets, permissions, status, generics

from .filter import PostFilter
from .pagination import PkPageNumberPagination
from rest_framework import filters
from rest_framework.filters import SearchFilter, OrderingFilter

from .models import Post, Comment, Like, Category
from .serializers import (
    PostSerializer,
    CommentSerializer,
    LikeSerializer,
    PostCreateSerializer,
    CommentCreateSerializer,
    CategorySerializer,

    #CartSerializer
)


class PostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.AllowAny]
    lookup_field = 'pk'
class PostCreateAPIView(generics.CreateAPIView):

    serializer_class = PostCreateSerializer
    permission_classes = [permissions.AllowAny]


class LikeCreateAPIView(generics.CreateAPIView):

    serializer_class = LikeSerializer
    permission_classes = [permissions.AllowAny]
class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (SearchFilter, OrderingFilter,)
    search_fields = ['title', 'content']
    pagination_class = PkPageNumberPagination
    permission_classes = [permissions.AllowAny]

class PostListCopy(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = (SearchFilter, OrderingFilter,)
    ordering_fields = ['created_at']
    search_fields = ['title', 'content']
    filterset_class = PostFilter
    pagination_class = PkPageNumberPagination
    permission_classes = [permissions.AllowAny]

class CommentViewSet(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentCreateSerializer
    permission_classes = [permissions.AllowAny]


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

#class CartAPIView(APIView):
#    permission_classes = [permissions.AllowAny]


    #def post(self, request):
    #    serializer = CartSerializer(data=request.data)
    #    if serializer.is_valid():
    #        serializer.save()
    #        return Response(serializer.data, status=status.HTTP_201_CREATED)
    #    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#class CartRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    #queryset = Cart.objects.all()
    #serializer_class = CartSerializer
    #permission_classes = [permissions.AllowAny]