from room.models import CardRoom
from userauth.models import User
from src.room_controller import Controller
from room.models import CardRoom
import pytest

def test_room_controller_adds_user_to_room_works(admin_user):
    controller = Controller()
    card_room = CardRoom.objects.create()

    controller.add_player(admin_user, card_room)

    room_users = card_room.players.all()

    assert len(room_users) == 1
    assert room_users[0] == admin_user

def test_room_controller_adds_user_to_room_raises_error_when_user_already_in_room(admin_user):
    controller = Controller()
    card_room = CardRoom.objects.create()

    controller.add_player(admin_user, card_room)

    with pytest.raises(ValueError):
        controller.add_player(admin_user, card_room)
