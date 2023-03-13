from django.db import models
from userauth.models import User


class CardRoom(models.Model):
    players = models.ManyToManyField(User)
    players_count = models.IntegerField(default=0)
    game_status = models.BooleanField(default=False)


class Stats(models.Model):
    room = models.OneToOneField(
        CardRoom, on_delete=models.CASCADE, related_name="stats"
    )
    board = models.CharField(max_length=20, blank=True)
    old_board = models.CharField(max_length=20, blank=True)
    trump_card = models.CharField(max_length=10, blank=True)
    team_one_score = models.IntegerField(default=0)
    team_two_score = models.IntegerField(default=0)
    player_position = models.IntegerField(default=0)
    played_card = models.CharField(max_length=4, blank=True)
    cards_per_round = models.IntegerField(default=0)
    winner = models.CharField(max_length=40, blank=True)
    last_played_card = models.DateTimeField(auto_now_add=True)
    players_choice = models.IntegerField(default=0)
    cards_in_play = models.IntegerField(default=0)
