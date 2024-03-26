from django.db import models

class City(models.Model):
    content = models.TextField(blank=False)
    weather = models.TextField()
    def __str__(self):
        return self.content
