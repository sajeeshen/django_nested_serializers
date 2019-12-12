from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewSets

router = DefaultRouter()
router.register('author', AuthorViewSets)

urlpatterns = [
    path('', include(router.urls))
]

