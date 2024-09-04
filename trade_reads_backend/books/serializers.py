from rest_framework import serializers
from useraccount.serializers import UserDetailSerializer

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'image_url')
        
class BookDetailSerializer(serializers.ModelSerializer):
    owner = UserDetailSerializer(read_only=True, many=False)
    class Meta:
        model = Book
        fields = ('id', 'title', 'description', 'author', 'language', 'pages', 'publisher', 'published_date', 'interested', 'image_url', 'owner')