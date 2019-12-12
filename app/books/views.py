from rest_framework import viewsets
from core.models import Book
from .serializers import BookSerializers


class BookViewSets(viewsets.ModelViewSet):
    """ View set for managing book related actions """
    queryset = Book.objects.all()
    serializer_class = BookSerializers
