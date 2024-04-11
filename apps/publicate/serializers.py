from django.db.models import Avg
from rest_framework import serializers
from apps.user.serializer import UserSerializer
from . import models
from .models import Post, Comment, Like, Category


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = "__all__"
class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['author', 'content']


class LikeSerializer(serializers.ModelSerializer):
    rating = serializers.IntegerField(min_value=1, max_value=5)

    class Meta:
        model = Like
        fields = '__all__'

    def create(self, validated_data):
        # Ensure that rating is within the allowed range
        rating = validated_data.get('rating')
        if rating not in range(1, 6):
            raise serializers.ValidationError("Rating must be between 1 and 5.")

        return Like.objects.create(**validated_data)
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'parent']
class PostSerializer(serializers.ModelSerializer):
    likes_count = serializers.SerializerMethodField()
    average_likes = serializers.SerializerMethodField()
    category = CategorySerializer()
    comments = serializers.SerializerMethodField()
    class Meta:
        model = Post
        fields = '__all__'

    def get_likes_count(self, obj):
        return obj.likes.count()

    def get_average_likes(self, obj):
        likes = Like.objects.filter(post=obj).aggregate(avg_rating=models.Avg('rating'))
        return likes['avg_rating'] if likes['avg_rating'] else 0

    def get_comments(self, obj):
        comments = Comment.objects.filter(post_id=obj.id)
        return CommentSerializer(comments, many=True).data







#class CartSerializer(serializers.ModelSerializer):

#    class Meta:
#        model = Cart
#        fields = "__all__"


