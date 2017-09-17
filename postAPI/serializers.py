from rest_framework import serializers
from django.contrib.auth.models import User as Author
from .models import Post

class PostSerializer(serializers.ModelSerializer):

    author = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Post
        fields = ('id',
                  'timestamp_posted',
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
        fields = ('id', 'username', 'email', 'posts', 'password',)
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        author = Author(
            email = validated_data['email'],
            username = validated_data['username']
        )
        author.set_password(validated_data['password'])
        author.save()
        return author

    def update(self, instance, validated_data):
        for attr, value in validated_data.items():
            if attr == 'password':
                instance.set_password(value)
            else:
                setattr(instance, attr, value)
        instance.save()
        return instance