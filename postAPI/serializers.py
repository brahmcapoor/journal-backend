from rest_framework import serializers
from django.contrib.auth.models import User as Author
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ('timestamp_posted',
                  'timestamp_edited',
                  'posted_text',
                  'edited_text',
                  'author',
                  'private')

class PostDateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('timestamp_posted',)

class AuthorSerializer(serializers.ModelSerializer):

    posts = serializers.PrimaryKeyRelatedField(many=True,
                                               queryset=Post.objects.all())

    class Meta:
        model = Author
        fields = ('id', 'username', 'posts')