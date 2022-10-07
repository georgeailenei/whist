import pytest
from whist.models import Player, GameStats
from src.database_repository import GameData


@pytest.mark.django_db
class TestDatabaseRepository:
    game = GameData()

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
        assert players_stats[hand] == [["Ac"], ["Kh"]]
        assert players_stats[tricks] == [2, 3]
        assert players_stats[played_hands] == [["2c"], ["5c"]]

    def test_remove_all_player_stats_when_database_is_populated_returns_empty_database(self):
        self.game.save_player_stats("George", "Ac", 2, "2c")
        self.game.save_player_stats("Robert", "Kh", 3, "5c")
        self.game.remove_all_players_stats()
        assert len(Player.objects.all()) == 0

    def test_save_all_player_stast_when_database_is_populated_returns_new_data_sets(self):
        self.game.save_player_stats("George", "Ac", 2, "2c")
        self.game.save_player_stats("Robert", "Kh", 3, "5c")
        self.game.save_all_players_stats(["Alex", "Dan"], ["2c", "3c"], [0, 0], ["Ah", "Kh"])

        players_stats = self.game.get_all_players_stats()
        names, hands, tricks, played_hands = 0, 1, 2, 3

        assert players_stats[names] == ["Alex", "Dan"]
        assert players_stats[hands] == [["2c"], ["3c"]]
        assert players_stats[tricks] == [0, 0]
        assert players_stats[played_hands] == [["Ah"], ["Kh"]]

    def test_get_game_stats_when_db_is_empty_return_none(self):
        game_stats = self.game.get_game_stats()
        assert game_stats is None

    def test_get_game_stats_when_db_is_populated_return_current_data(self):
        GameStats.objects.create(
            board="Ah Kc",
            trump_card="clubs",
            team_one_score=0,
            team_two_score=0,
            player_position=1
        )
        board, trump_card, score1, score2, pos = 0, 1, 2, 3, 4
        game_stats = self.game.get_game_stats()
        assert game_stats[board] == ["Ah", "Kc"]
        assert game_stats[trump_card] == "clubs"
        assert game_stats[score1] == 0
        assert game_stats[score2] == 0
        assert game_stats[pos] == 1

    def test_remove_game_stats_when_db_is_populated_returns_empty_db(self):
        GameStats.objects.create(
            board="Ah Kc",
            trump_card="clubs",
            team_one_score=0,
            team_two_score=0,
            player_position=1
        )
        self.game.remove_game_stats()
        assert GameStats.objects.count() == 0

    def test_save_game_stats_when_db_is_populated_returns_given_data(self):
        GameStats.objects.create(
            board="Ah Kc",
            trump_card="clubs",
            team_one_score=0,
            team_two_score=0,
            player_position=1
        )
        self.game.save_game_stats("2c 3c", "hearts", 1, 2, 0)
        stats = self.game.get_game_stats()
        board, trump_card, score1, score2, pos = 0, 1, 2, 3, 4
        assert stats[board] == ["2c", "3c"]
