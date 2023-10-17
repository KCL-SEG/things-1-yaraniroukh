from django.db import models
from django.db.models import Model
from django.core.validators import MinValueValidator
from django.core.validators import MaxValueValidator

class Thing(Model):
    name = models.CharField(unique=True, blank=False, max_length=30)
    description = models.CharField(unique=False, blank=True, max_length=120)
    quantity = models.IntegerField(unique=False, validators=[MinValueValidator(0, "Must be at least 0"), MaxValueValidator(100, "Must be at most 100")], )

