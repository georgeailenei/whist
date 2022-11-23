from rest_framework import fields
from rest_framework.serializers import ModelSerializer, Serializer
from .models import CardRoom, Stats
from userauth.models import User


class PlayerSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = "id", "hand", "username", "tricks", "played_hand"

    hand = fields.SerializerMethodField()

    def get_hand(self, object):
        return object.hand.split()


class StatsSerializer(ModelSerializer):
    class Meta:
        model = Stats
        fields = "__all__"

    board = fields.SerializerMethodField()
    played_card = fields.SerializerMethodField()

    def get_board(self, object):
        return object.board.split()

    def get_played_card(self, object):
        return object.played_card.split()


class RoomSerializer(ModelSerializer):
    class Meta:
        model = CardRoom
        fields = "__all__"

    players = PlayerSerializer(many=True)
    stats = StatsSerializer()


class CardSerializer(Serializer):
    card = fields.CharField()
