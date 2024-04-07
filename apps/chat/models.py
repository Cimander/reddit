from django.db import models
from apps.user.models import User

class Group(models.Model):
    name = models.CharField(max_length=100)
    members = models.ManyToManyField(User, related_name='chat_groups')

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)