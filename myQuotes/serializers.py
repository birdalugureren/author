from rest_framework import serializers
from myQuotes.models import Author
from django.contrib.auth.models import User


class AuthorSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Author
        fields = ('id', 'author', 'text', 'tags', 'owner')


class UserSerializer(serializers.ModelSerializer):
    authors = serializers.PrimaryKeyRelatedField(many=True, queryset=Author.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'authors')