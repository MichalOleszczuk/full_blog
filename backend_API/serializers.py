from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Post
        fields = ('url', 'pk', 'highlight', 'owner', 'title', 'text', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    posts = serializers.HyperLinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'pk', 'username', 'posts', 'comments')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    comments = serializers.HyperlinkedIdentityField(view_name='snippet-detail', )
    owner = serializers.ReadOnlyField(source='owner.username')
    title = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Comment
        fields = ('url', 'pk', 'owner', 'text', 'title')