from rest_framework import fields
from rest_framework.serializers import ModelSerializer, Serializer

from room.models import CardRoom
from userauth.models import User


class PlayerSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class RoomSerializer(ModelSerializer):
    class Meta:
        model = CardRoom
        fields = '__all__'

    players = PlayerSerializer(many=True)


class CardSerializer(Serializer):
    card = fields.CharField()
