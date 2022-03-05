from django.urls import include, path
from django.db import router

from .views import BookViewSet, PublisherViewSet, CategoryViewSet, AuthorViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'books', BookViewSet, basename="books")
router.register(r'publisher', PublisherViewSet, basename="publisher")
router.register(r'category', CategoryViewSet, basename='category')
router.register(r'author', AuthorViewSet, basename='author')


urlpatterns = [
    path('', include(router.urls)),
]
