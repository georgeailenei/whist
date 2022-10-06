import pytest
from whist.models import Player
from src.database_repository import Game


class TestDatabaseRepository:
    def test_simple(self):
        a = 1
        b = 2
        assert a + b == 3

    @pytest.mark.django_db
    def test_save_player_stats_when_receiving_data_returns_the_given_data(self):
        the_game = Game()
        the_game.save_player_stats("Dan", "Ah", 0, "Kc", 1)
        the_game.save_player_stats("Alex", "Ah", 0, "Kc", 1)
        players = Player.objects.all()
        players_names = {p.name for p in players}
        assert len(players) == 2
        assert players_names == {"Dan", "Alex"}
