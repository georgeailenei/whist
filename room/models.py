from django.db import models
from userauth.models import User


class CardRoom(models.Model):
    players = models.ManyToManyField(User)
    status = models.BooleanField(default=True)
    seats = models.CharField(max_length=15, default="Available")
    players_count = models.IntegerField(default=0)
