from rest_framework import serializers
from core.models import Author


class AuthorSerializers(serializers.ModelSerializer):
    """ Serializer for Author """

    class Meta:
        model = Author
        fields = ('name', 'active', 'slug',)
