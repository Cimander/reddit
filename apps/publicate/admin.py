from django.contrib import admin
from .models import Cart, Post, Comment

admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Cart)