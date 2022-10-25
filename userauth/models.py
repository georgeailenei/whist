from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager


class User(AbstractUser, PermissionsMixin):
    hand = models.CharField(max_length=50)
    tricks = models.IntegerField()
    played_cards = models.CharField(max_length=50)
