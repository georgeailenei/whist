from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin


class User(AbstractUser, PermissionsMixin):
    hand = models.CharField(max_length=80, default="")
    tricks = models.IntegerField(default=0)
    played_hand = models.CharField(max_length=80, default="")
    choice = models.IntegerField(default=0)
    registration_date = models.DateTimeField(auto_now_add=True)
    points = models.IntegerField(default=1000)
    rank = models.IntegerField(default=0)