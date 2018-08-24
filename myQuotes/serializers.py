from rest_framework import serializers
from myQuotes.models import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'author', 'text', 'tags')
