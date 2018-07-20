from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from foodstuff.models import FoodStuff


class User(AbstractUser):
    AUTHORITY = (
        ('C', 'Customer'),
        ('O', 'Owner')
    )

    email = models.EmailField(blank=True)
    authority = models.CharField(max_length=1, choices=AUTHORITY)
    order = models.ForeignKey(
        FoodStuff,
        on_delete=models.CASCADE,
        null=True,
        blank=True,

    )




