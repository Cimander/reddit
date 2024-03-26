from django.contrib import admin
from .models import Cart, Post, Comment, Category

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Cart)
admin.site.register(Category)