from django.db import models
from django.db.models.base import Model


class Post(models.Model):
    content = models.CharField(max_length=100)
    author = models.CharField(max_length=40, null=False)
    created = models.DateTimeField(auto_now_add=True)
    url = models.URLField(max_length=200, null=False,
                          default="https://www.google.com/")
    upvote = models.IntegerField(default=0)


class comments(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=False)
    author_name = models.CharField(max_length=40, null=False)
    created = models.DateField(auto_now_add=True)
    content = models.TextField(max_length=100, null=False)
