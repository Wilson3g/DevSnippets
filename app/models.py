from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse, reverse_lazy
from datetime import datetime, time


class Post(models.Model):
    title = models.CharField(max_length=255)
    title_tag = models.CharField(max_length=255, default='DevSnippets | Tecnologia e informação')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title + ' | ' + str(self.author)

    def get_absolute_url(self):
        return reverse('update_post', args=[str(self.id)])
