from django.contrib.auth.models import User

from rest_framework import serializers

from .models import Post, Upvote, Comment


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'password', 'email')

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = [
            'id', 'title', 'link', 'num_upvotes', 'author', 'creation_date'
        ]
        extra_kwargs = {
            'num_upvotes': {'read_only': True},
            'author': {'read_only': True},
        }

    def create(self, validated_data):
        author_id = self.context['request'].user.pk
        validated_data['author_id'] = author_id
        post = super().create(validated_data)
        return post


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id', 'author', 'content', 'creation_date']
        extra_kwargs = {
            'author': {'read_only': True},
        }

    def create(self, validated_data):
        author_id = self.context['request'].user.pk
        post_id = self.context['view'].kwargs['pk']

        validated_data['author_id'] = author_id
        validated_data['post_id'] = post_id

        comment = super().create(validated_data)
        return comment


class UpvoteSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    post = PostSerializer()

    class Meta:
        model = Upvote
        fields = '__all__'
