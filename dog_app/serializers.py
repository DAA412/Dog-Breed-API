from rest_framework import serializers
from django.db.models import Avg, Count, OuterRef, Subquery
from .models import Dog, Breed


class BreedSerializer(serializers.ModelSerializer):
    dogs_count = serializers.SerializerMethodField()

    class Meta:
        model = Breed
        fields = [
            'id', 'name', 'size', 'friendliness', 'trainability',
            'shedding_amount', 'exercise_needs', 'dogs_count'
        ]

    def get_dogs_count(self, obj):
        return getattr(obj, 'dogs_count', 0)


class BreedDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = '__all__'


class BreedSimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Breed
        fields = [
            'name', 'size', 'friendliness', 'trainability',
            'shedding_amount', 'exercise_needs'
        ]


class DogSerializer(serializers.ModelSerializer):
    breed_name = serializers.CharField(source='breed.name', read_only=True)
    avg_breed_age = serializers.SerializerMethodField()

    class Meta:
        model = Dog
        fields = [
            'id', 'name', 'age', 'breed', 'breed_name', 'gender', 'color',
            'favorite_food', 'favorite_toy', 'avg_breed_age'
        ]

    def get_avg_breed_age(self, obj):
        return getattr(obj, 'avg_breed_age', None)


class DogDetailSerializer(serializers.ModelSerializer):
    breed_info = BreedSimpleSerializer(source='breed', read_only=True)
    same_breed_count = serializers.SerializerMethodField()

    class Meta:
        model = Dog
        fields = [
            'id', 'name', 'age', 'breed', 'breed_info', 'gender', 'color',
            'favorite_food', 'favorite_toy', 'same_breed_count'
        ]

    def get_same_breed_count(self, obj):
        return getattr(obj, 'same_breed_count', 0)
