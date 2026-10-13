from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):

    ROLE_CHOICES = (
        ('CUSTOMER', 'Customer'),
        ('STAFF', 'Staff'),
        ('ADMIN', 'Admin'),
    )

    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True)

    role = models.CharField(
        max_length=10,
        choices=ROLE_CHOICES,
        default='CUSTOMER'
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.email