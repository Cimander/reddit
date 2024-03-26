from django.db.models import Avg
from django.db import models
from django.utils import timezone
from apps.user.models import User

from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(max_length=100)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']

    def __str__(self):
        return self.name





class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    title = models.CharField(max_length=300)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title

    def add_to_favorite(self, user):
        cart, created = Cart.objects.get_or_create(user=user)
        cart.posts.add(self)

    def remove_from_favorite(self, user):
        cart, created = Cart.objects.get_or_create(user=user)
        cart.posts.remove(self)
class Like(models.Model):
    post = models.ForeignKey(Post, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveSmallIntegerField(choices=[(i, i) for i in range(1, 5)])







class Comment(models.Model):
    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
   
#class Comment(models.Model):
#    content = models.TextField()
#    created_at = models.DateTimeField(auto_now_add=True)
#    post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)  # замените 'yourappname' на имя вашего приложения
#    author = models.ForeignKey(User, on_delete=models.CASCADE)  # добавляем поле для автора

#    def __str__(self):
#        return self.content



class Cart(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    post = models.ManyToManyField(Post)


