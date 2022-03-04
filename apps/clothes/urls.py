from django.urls import include, path
from django.db import router

from .views import BrandViewSet, ClothesViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'clothes', ClothesViewSet, basename="clothes")
router.register(r'brand', BrandViewSet, basename="brand")


urlpatterns = [
    path('', include(router.urls)),
]
