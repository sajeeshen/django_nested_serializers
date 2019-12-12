from rest_framework import serializers
from core.models import Book


class BookCreateSerializers(serializers.ModelSerializer):
    """ Serializer for Creating Book Object """
    class Meta:
        model = Book
        fields = ('name', 'author', 'publisher', 'slug')


class BookListSerializers(serializers.ModelSerializer):
    """ Serializers for listing books with publisher and author"""
    author = serializers.StringRelatedField()
    publisher = serializers.StringRelatedField()
    class Meta:
        model = Book
        fields = ('name', 'author', 'publisher', 'slug')

