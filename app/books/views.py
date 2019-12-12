from rest_framework import viewsets
from core.models import Book
from .serializers import BookCreateSerializers, BookListSerializers


class BookViewSets(viewsets.ModelViewSet):
    """ View set for managing book related actions """
    queryset = Book.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.action == "create":
            return BookCreateSerializers

        return BookListSerializers
