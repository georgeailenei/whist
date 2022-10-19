from django.db import models
from userauth.models import User


class CardRoom(models.Model):
    player_name = models.ManyToManyField(User)
    status = models.CharField(max_length=7)
