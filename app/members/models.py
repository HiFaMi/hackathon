from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.


class User(AbstractUser):
    AUTHORITY = (
        ('C', 'Customer'),
        ('O', 'Owner')
    )

    email = models.EmailField(blank=True)
    authority = models.CharField(max_length=1, choices=AUTHORITY)
    # order = models.ManyToManyField()
