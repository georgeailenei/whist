import dataclasses
from random import shuffle
from typing import List

from room.models import CardRoom
from userauth.models import User


class Deck:
    def __init__(self):
        self.cards = [
            "Ah",
            "Kh",
            "Qh",
            "Jh",
            "10h",
            "9h",
            "8h",
            "7h",
            "6h",
            "5h",
            "4h",
            "3h",
            "2h",
            "Ac",
            "Kc",
            "Qc",
            "Jc",
            "10c",
            "9c",
            "8c",
            "7c",
            "6c",
            "5c",
            "4c",
            "3c",
            "2c",
            "As",
            "Ks",
            "Qs",
            "Js",
            "10s",
            "9s",
            "8s",
            "7s",
            "6s",
            "5s",
            "4s",
            "3s",
            "2s",
            "Ad",
            "Kd",
            "Qd",
            "Jd",
            "10d",
            "9d",
            "8d",
            "7d",
            "6d",
            "5d",
            "4d",
            "3d",
            "2d",
        ]
        self.shuffle()

    def shuffle(self):
        shuffle(self.cards)


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit

    def __str__(self):
        return f"{self.rank}{self.suit}"
