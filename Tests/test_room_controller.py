from room.models import CardRoom
from userauth.models import User
from src.room_controller import Controller
from room.models import CardRoom
import pytest


def test_room_controller_adds_user_to_room_works(admin_user):
    controller = Controller()
    card_room = CardRoom.objects.create(status=False, players_count=0)
    controller.add_player(admin_user, card_room)
    room_users = card_room.players.all()

    assert len(room_users) == 1
    assert room_users[0] == admin_user


def test_room_controller_adds_user_to_room_raises_error_when_user_already_in_room(admin_user):
    controller = Controller()
    card_room = CardRoom.objects.create(status=False, players_count=0)
    controller.add_player(admin_user, card_room)
    with pytest.raises(ValueError):
        controller.add_player(admin_user, card_room)


def test_room_controller_players_waiting_when_users_already_in_room(admin_user):
    controller = Controller()
    card_room = CardRoom.objects.create(status=False, players_count=0)
    controller.add_player(admin_user, card_room)
    rooms = CardRoom.objects.all()
    count = controller.players_waiting(rooms)
    assert count == [1]


def test_room_controller_players_waiting_when_users_already_in_rooms(admin_user):
    controller = Controller()
    card_room = CardRoom.objects.create(status=False, players_count=0)
    controller.add_player(admin_user, card_room)
    card_room = CardRoom.objects.create(players_count=0)
    controller.add_player(admin_user, card_room)
    rooms = CardRoom.objects.all()
    count = controller.players_waiting(rooms)
    assert count == [1, 1]


def test_room_controller_add_player_when_adding_players_it_updates_players_count_too(admin_user):
    controller = Controller()
    card_room = CardRoom.objects.create(players_count=0)
    controller.add_player(admin_user, card_room)
    assert card_room.players_count == 1


def test_room_controller_add_player_when_adding_players_it_updates_status_too(admin_user):
    controller = Controller()
    card_room = CardRoom.objects.create(players_count=0)
    controller.add_player(admin_user, card_room)
    assert card_room.status is True


def test_room_controller_add_player_when_adding_players_it_updates_seats_too(admin_user):
    # Ask Dan about how you can add more users in db to tests.
    controller = Controller()
    card_room = CardRoom.objects.create()
    controller.add_player(admin_user, card_room)
    assert card_room.seats == "Available"
