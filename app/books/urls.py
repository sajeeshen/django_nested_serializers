from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import BookViewSets

app_name = "books"
router = DefaultRouter()
router.register('books', BookViewSets)
urlpatterns = [
    path('', include(router.urls))
]
