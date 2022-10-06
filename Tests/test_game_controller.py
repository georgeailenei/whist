import pytest
from whist.models import Player
from whist.game_logic.services.controller import Controller
from whist.game_logic.domain.validate import ValidateCards
from src.database_repository import GameData


@pytest.mark.django_db
class TestController:
    controller = Controller(ValidateCards(), GameData())

    def test_load_players_stats_from_db_when_loading_from_empty_db_returns_empty_lists_and_zeros(self):
        players_stats = self.controller.load_players_stats_from_db()

        assert players_stats['players_names'] == ["George", "Alex", "Dan", "Robert"]
        assert players_stats['players_cards'] == [[], [], [], []]
        assert players_stats['players_tricks'] == [0, 0, 0, 0]
        assert players_stats['removed_players_cards'] == [[], [], [], []]

    def test_load_players_stats_from_db_when_loading_from_populated_db_return_the_current_data_from_db(self):
        player1 = Player.objects.create(name="Alex", hand="Ah, Kc, 2c", tricks=0, played_cards="2c, 3c")
        player2 = Player.objects.create(name="Gicu", hand="Ac, 3c, 5c", tricks=2, played_cards="Jh, Jc")
        player3 = Player.objects.create(name="NeaCaiSa", hand="10h, 7c, 6c", tricks=1, played_cards="Qc, Qh")
        player4 = Player.objects.create(name="Carlos", hand="2h, 3h, 4h", tricks=0, played_cards="8c, 8h")

        players_stats = self.controller.load_players_stats_from_db()
        assert players_stats['players_names'] == ["Alex", "Gicu", "NeaCaiSa", "Carlos"]
        assert players_stats['players_cards'] == [["Ah", "Kc", "2c"], ["Ac", "3c", "5c"], ["10h", "7c", "6c"], ["2h", "3h", "4h"]]
        assert players_stats['players_tricks'] == [0, 2, 1, 0]
        assert players_stats['removed_players_cards'] == [["2c", "3c"], ["Jh", "Jc"], ["Qc", "Qh"], ["8c", "8h"]]

    def test_load_players_when_db_is_empty_returns_example_names_and_empty_lists(self):
        players = self.controller.load_players()
        player_one, player_two, player_three, player_four = 0, 1, 2, 3

        assert players[player_one].name == "George"
        assert players[player_four].tricks == 0
        assert players[player_two].cards == []
        assert players[player_three].remove_cards == []

    def test_load_players_when_db_is_populated_returns_current_players_data(self):
        player1 = Player.objects.create(name="Alex", hand="Ah, Kc, 2c", tricks=0, played_cards="2c, 3c")
        player2 = Player.objects.create(name="Gicu", hand="Ac, 3c, 5c", tricks=2, played_cards="Jh, Jc")
        player3 = Player.objects.create(name="NeaCaiSa", hand="10h, 7c, 6c", tricks=1, played_cards="Qc, Qh")
        player4 = Player.objects.create(name="Carlos", hand="2h, 3h, 4h", tricks=0, played_cards="8c, 8h")

        players = self.controller.load_players()
        player_one, player_two, player_three, player_four = 0, 1, 2, 3

        assert players[player_one].name == "Alex"
        assert players[player_four].tricks == 0
        assert players[player_two].cards == ["Ac", "3c", "5c"]
        assert players[player_three].remove_cards == ["Qc", "Qh"]
