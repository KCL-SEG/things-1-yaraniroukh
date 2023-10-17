from django.db import models
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator
from django.contrib.auth.models import AbstractUser

class Thing(AbstractUser):
    name = models.CharField(unique=True, blank=False, max_length=30)
    description = models.CharField(unique=False, blank=True, max_length=120)
    quantity = models.IntegerField(unique=False, validators=[MinValueValidator(0, "Must be at least 0"), MaxValueValidator(100, "Must be at most 100")], )

