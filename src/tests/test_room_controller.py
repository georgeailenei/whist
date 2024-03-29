from room.controllers.room_controller import Controller
from room.models import CardRoom
import pytest

#
# def test_room_controller_adds_user_to_room_works(admin_user):
#     controller = Controller()
#     card_room = CardRoom.objects.create(status=False, players_count=0)
#     controller.add_player(admin_user, card_room)
#     room_users = card_room.players.all()
#
#     assert len(room_users) == 1
#     assert room_users[0] == admin_user
#
#
# def test_room_controller_adds_user_to_room_raises_error_when_user_already_in_room(
#     admin_user,
# ):
#     controller = Controller()
#     card_room = CardRoom.objects.create(status=False, players_count=0)
#     controller.add_player(admin_user, card_room)
#     with pytest.raises(ValueError):
#         controller.add_player(admin_user, card_room)
#
#
# def test_room_controller_add_player_when_adding_players_it_updates_players_count_too(
#     admin_user,
# ):
#     controller = Controller()
#     card_room = CardRoom.objects.create(players_count=0)
#     controller.add_player(admin_user, card_room)
#     assert card_room.players_count == 1
#
#
# def test_room_controller_add_player_when_adding_players_it_updates_status_too(
#     admin_user,
# ):
#     controller = Controller()
#     card_room = CardRoom.objects.create(players_count=0)
#     controller.add_player(admin_user, card_room)
#     assert card_room.status is True
#
#
# def test_room_controller_add_player_when_adding_players_it_updates_seats_too(
#     admin_user,
# ):
#     # Ask Dan about how you can add more users in db to tests.
#     controller = Controller()
#     card_room = CardRoom.objects.create()
#     controller.add_player(admin_user, card_room)
#     assert card_room.seats == "Available"
#
#
# def test_room_controller_remove_player_when_in_db(admin_user):
#     controller = Controller()
#     card_room = CardRoom.objects.create()
#     controller.add_player(admin_user, card_room)
#     controller.remove_player(admin_user, card_room)
#     assert card_room.players.count() == 0
#
#
# def test_room_controller_change_status_to_false_when_room_is_full(admin_user):
#     controller = Controller()
#     card_room = CardRoom.objects.create()
#     controller.add_player(admin_user, card_room)
#     the_room = CardRoom.objects.all().first()
#     controller.change_status_to_false(the_room)
#     assert the_room.status is False
