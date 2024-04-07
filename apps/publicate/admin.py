from django.contrib import admin
from .models import Cart, Post, Comment, Category
#class PostAdmin(admin.ModelAdmin):
#    filter_horizontal = ('category',)  # Добавляет виджет выбора множественных категорий

admin.site.register(Post)
admin.site.register(Category)

admin.site.register(Comment)
admin.site.register(Cart)
