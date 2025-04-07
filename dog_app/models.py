from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Breed(models.Model):
    SIZE_CHOICES = [
        ('Tiny', 'Tiny'),
        ('Small', 'Small'),
        ('Medium', 'Medium'),
        ('Large', 'Large'),
    ]

    name = models.CharField(max_length=100, unique=True)
    size = models.CharField(max_length=10, choices=SIZE_CHOICES)
    friendliness = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    trainability = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    shedding_amount = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    exercise_needs = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Breed'
        verbose_name_plural = 'Breeds'


class Dog(models.Model):
    GENDER_CHOICES = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.ForeignKey(
        Breed,
        on_delete=models.CASCADE,
        related_name='dogs'
    )
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    color = models.CharField(max_length=50)
    favorite_food = models.CharField(max_length=100)
    favorite_toy = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} ({self.breed.name})"

    class Meta:
        verbose_name = 'Dog'
        verbose_name_plural = 'Dogs'