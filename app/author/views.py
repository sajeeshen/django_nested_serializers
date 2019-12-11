from django.shortcuts import render
from rest_framework import viewsets
from core.models import Author
from .serializers import AuthorSerializers

# Create your views here.


class AuthorViewSets(viewsets.ModelViewSet):
    """ View set for managing the Author """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializers
