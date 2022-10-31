from room.models import CardRoom
from src.database_repo import GameData
import pytest


def test_load_game_stats_when_database_is_empty_returns_default_model_settings(admin_user):
    repo = GameData()
    CardRoom.objects.create()
    card_room = CardRoom.objects.all().first()
    card_room.players.add(admin_user)
    room_stats = repo.load_game_stats(card_room)

    assert room_stats['player_pos'] == 0
    assert room_stats['board'] == ""
    assert room_stats['players_tricks'] == [0]
