from django.db import models


class Player(models.Model):
    name = models.CharField(max_length=30)
    hand = models.CharField(max_length=50)
    tricks = models.IntegerField()
    played_cards = models.CharField(max_length=50)


class GameStats(models.Model):
    board = models.CharField(max_length=20)
    trump_card = models.CharField(max_length=10)
    team_one_score = models.IntegerField()
    team_two_score = models.IntegerField()
    player_position = models.IntegerField()
