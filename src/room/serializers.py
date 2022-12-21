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
        if self.context['request'].user == object:
            return object.hand.split()
        else:
            return len(object.hand.split()) * ['not_permitted']


class StatsSerializer(ModelSerializer):
    class Meta:
        model = Stats
        fields = "__all__"

    board = fields.SerializerMethodField()
    played_card = fields.SerializerMethodField()
    old_board = fields.SerializerMethodField()

    def get_board(self, object):
        return object.board.split()

    def get_old_board(self, object):
        return object.old_board.split()

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


class ChoiceSerializer(Serializer):
    choice = fields.BooleanField()


class PlayerSerializer(Serializer):
    player = fields.CharField()
