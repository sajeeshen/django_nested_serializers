from rest_framework import serializers
from core.models import Book


class BookSerializers(serializers.ModelSerializer):
    """ Serializer for Books """
    author = serializers.StringRelatedField()
    publisher = serializers.StringRelatedField()

    class Meta:
        model = Book
        fields = ('name', 'author', 'publisher', 'slug')
