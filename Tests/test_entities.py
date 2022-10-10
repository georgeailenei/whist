import pytest
from whist.game_logic.services.controller import Controller
from whist.game_logic.domain.validate import ValidateCards
from src.database_repository import GameData
from whist.game_logic.domain.entity import Player


class TestControllerAndEntities:
    controller = Controller(ValidateCards(), GameData())

    def test_remove_card_from_player_when_given_a_card_return_a_new_list_without_that_car(self):
        player1 = Player("George")
        player2 = Player("Dan")
        player3 = Player("Robert")
        player4 = Player("Nicu")

        players = [player1, player2, player3, player4]
        player2.cards.append("8c")
        player2.cards.append("2c")
        player2.cards.append("Ac")

        card_received = "2c"
        self.controller.remove_card_from_player(card_received, players)
        assert player2.cards == ["8c", "Ac"]
