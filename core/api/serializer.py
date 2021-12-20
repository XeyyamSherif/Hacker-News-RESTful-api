from django.db import models
from rest_framework import fields, serializers
from .models import Post, comments


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ("id", "content", "author", "upvote", "url")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comments
        fields = ("id", "content", "author_name")


