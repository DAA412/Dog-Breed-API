from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BreedViewSet, DogViewSet

router = DefaultRouter()
router.register(r'breeds', BreedViewSet, basename='breed')
router.register(r'dogs', DogViewSet, basename='dog')

urlpatterns = [
    path('api/', include(router.urls)),
]