from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models import Avg, Count, OuterRef, Subquery
from .models import Dog, Breed
from .serializers import (
    BreedSerializer, BreedDetailSerializer,
    DogSerializer, DogDetailSerializer
)


class BreedViewSet(viewsets.ModelViewSet):
    queryset = Breed.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BreedDetailSerializer
        return BreedSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.action == 'list':
            queryset = queryset.annotate(
                dogs_count=Count('dogs')
            )
        return queryset


class DogViewSet(viewsets.ModelViewSet):
    queryset = Dog.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return DogDetailSerializer
        return DogSerializer

    def get_queryset(self):
        queryset = super().get_queryset()

        if self.action == 'list':
            queryset = queryset.annotate(
                avg_breed_age=Subquery(
                    Dog.objects.filter(breed=OuterRef('breed'))
                    .values('breed')
                    .annotate(avg_age=Avg('age'))
                    .values('avg_age')[:1]
                )
            )
        elif self.action == 'retrieve':
            queryset = queryset.annotate(
                same_breed_count=Subquery(
                    Dog.objects.filter(breed=OuterRef('breed'))
                    .exclude(id=OuterRef('id'))
                    .values('breed')
                    .annotate(count=Count('id'))
                    .values('count')[:1]
                )
            )
        return queryset
