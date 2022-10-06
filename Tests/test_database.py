import pytest
from whist.models import Player
from src.database_repository import Game


@pytest.mark.django_db
class TestDatabaseRepository:
    game = Game()

    def test_save_player_stats_when_receiving_data_returns_the_given_data(self):
        self.game.save_player_stats("Dan", "Ah", 0, "Kc")
        self.game.save_player_stats("Alex", "Kh", 0, "Kc")

        players = Player.objects.all()
        players_names = {p.name for p in players}
        players_hand = {p.hand for p in players}
        player_tricks = {p.tricks for p in players}

        assert len(players) == 2
        assert players_names == {"Dan", "Alex"}
        assert players_hand == {"Ah", "Kh"}
        assert player_tricks == {0, 0}

    def test_get_all_players_stats_when_database_is_empty_returns_none(self):
        players_stats = self.game.get_all_players_stats()
        assert players_stats is None

    def test_get_all_players_stats_when_database_is_populated_returns_the_current_data(self):
        self.game.save_player_stats("George", "Ac", 2, "2c")
        self.game.save_player_stats("Robert", "Kh", 3, "5c")

        players_stats = self.game.get_all_players_stats()
        name, hand, tricks, played_hands = 0, 1, 2, 3
        assert players_stats[name] == ["George", "Robert"]
        assert players_stats[hand] == ["Ac", "Kh"]
        assert players_stats[tricks] == [2, 3]
        assert players_stats[played_hands] == ["2c", "5c"]

    def test_remove_all_when_database_is_populated_returns_empty_database(self):
        self.game.save_player_stats("George", "Ac", 2, "2c")
        self.game.save_player_stats("Robert", "Kh", 3, "5c")
        self.game.remove_all()
        assert len(Player.objects.all()) == 0

    def test_save_all_when_database_is_populated_returns_new_data_sets(self):
        self.game.save_player_stats("George", "Ac", 2, "2c")
        self.game.save_player_stats("Robert", "Kh", 3, "5c")
        self.game.save_all(["Alex", "Dan"], ["2c", "3c"], [0, 0], ["Ah", "Kh"])

        players_stats = self.game.get_all_players_stats()
        names, hands, tricks, played_hands = 0, 1, 2, 3

        assert players_stats[names] == ["Alex", "Dan"]
        assert players_stats[hands] == ["2c", "3c"]
        assert players_stats[tricks] == [0, 0]
        assert players_stats[played_hands] == ["Ah", "Kh"]
