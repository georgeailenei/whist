from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class User(AbstractUser, PermissionsMixin):
    hand = models.CharField(max_length=80, default="")
    tricks = models.IntegerField(default=0)
    played_hand = models.CharField(max_length=80, default="")
    choice = models.IntegerField(default=0)
