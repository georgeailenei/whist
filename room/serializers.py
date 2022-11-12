from rest_framework.serializers import ModelSerializer

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
