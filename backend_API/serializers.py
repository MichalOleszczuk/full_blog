from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User


class PostSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='post-highlight', format='html')
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)

    class Meta:
        model = Post
        fields = ('url', 'pk', 'highlight', 'owner', 'title', 'text', 'linenos', 'language', 'style', 'comments')


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    title = serializers.ReadOnlyField(source='post.title')

    class Meta:
        model = Comment
        fields = ('post', 'url', 'pk', 'owner', 'text', 'title')


class UserSerializer(serializers.ModelSerializer):
    posts = serializers.HyperlinkedRelatedField(many=True, view_name='post-detail', read_only=True)
    password = serializers.CharField(write_only=True)
    comments = serializers.HyperlinkedRelatedField(many=True, view_name='comment-detail', read_only=True)

    class Meta:
        model = User
        read_only_fields = ('id',)
        fields = ('id', 'username', 'password', 'posts', 'comments', 'url')

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data.get('email', ''),
        )

        user.set_password(validated_data['password'])
        user.save()

        return user