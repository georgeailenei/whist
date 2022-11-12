from random import shuffle

from django.db import models
from userauth.models import User


class CardRoom(models.Model):
    players = models.ManyToManyField(User)
    status = models.BooleanField(default=True)
    seats = models.CharField(max_length=15, default="Available")
    players_count = models.IntegerField(default=0)


class Stats(models.Model):
    room = models.ForeignKey(CardRoom, on_delete=models.CASCADE)
    board = models.CharField(max_length=20, blank=True)
    trump_card = models.CharField(max_length=10, blank=True)
    team_one_score = models.IntegerField(default=0)
    team_two_score = models.IntegerField(default=0)
    player_position = models.IntegerField(default=0)
    played_card = models.CharField(max_length=4, blank=True)
