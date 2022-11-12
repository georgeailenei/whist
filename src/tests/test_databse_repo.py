from room.models import CardRoom
from room.repos.database_repo import GameData
import pytest


def test_load_game_stats_when_database_is_empty_returns_default_model_settings(admin_user):
    repo = GameData()
    CardRoom.objects.create()
    card_room = CardRoom.objects.all().first()
    card_room.players.add(admin_user)
    room_stats = repo.load_game_stats(card_room)

    assert room_stats['player_pos'] == 0
    assert room_stats['board'] == ""
    assert room_stats['players'] == ['admin']


def test_save_played_card_when_database_receives_data_returns_the_given_data(admin_user):
    repo = GameData()
    CardRoom.objects.create()
    card_room = CardRoom.objects.all().first()
    card_room.players.add(admin_user)
    repo.save_played_card("Ah", card_room)


def test_get_room_stats_with_new_room_returns_stats_for_that_room(admin_user):
    repo = GameData()
    card_room = CardRoom.objects.create()
    card_room.players.add(admin_user)
    card_room = CardRoom.objects.all().first()

    room_stats = repo.get_room_stats(card_room)
    assert room_stats.room.players.all()[0] == admin_user
    assert room_stats.played_card == ""


@pytest.mark.django_db
def test_save_played_card_when_receiving_new_data_saves_received_data():
    repo = GameData()
    CardRoom.objects.create()
    card_room = CardRoom.objects.all().first()

    card = "Ah"
    repo.save_played_card(card, card_room)

    room_stats = repo.get_room_stats(card_room)
    assert room_stats.played_card == "Ah"
