import pytest
from whist.game_logic.services.controller import Controller
from whist.game_logic.domain.validate import ValidateCards
from src.database_repository import GameData
from whist.game_logic.domain.entity import Player


class TestControllerAndEntities:
    controller = Controller(ValidateCards(), GameData())

    def test_remove_card_from_player_when_given_a_card_return_a_new_list_without_that_card(self):
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
        assert player2.remove_cards == ["2c"]

    def test_find_winner_card_when_card_is_received_returns_the_right_name(self):
        player1 = Player("George")
        player2 = Player("Dan")
        player3 = Player("Robert")
        player4 = Player("Nicu")
        players = [player1, player2, player3, player4]

        player3.remove_cards.append("Ah")
        winner = "Ah"

        winner_name = self.controller.find_winner(winner, players)
        assert winner_name == "Robert"

    def test_add_trick_to_player_when_receiving_winner_name_returns_a_different_number_in_tricks_for_the_winner(self):
        player1 = Player("George")
        player2 = Player("Dan")
        player3 = Player("Robert")
        player4 = Player("Nicu")

        players = [player1, player2, player3, player4]
        winner = "Robert"
        current_players = self.controller.add_trick_to_player(winner, players)
        assert current_players[2].tricks == 1

    def test_winner_table_position_returns_the_winner_index_in_the_list(self):
        player1 = Player("George")
        player2 = Player("Dan")
        player3 = Player("Robert")
        player4 = Player("Nicu")

        players = [player1, player2, player3, player4]
        winner1, winner2, winner3, winner4 = "George", "Dan", "Robert", "Nicu"
        player_pos1 = self.controller.winner_table_position(winner1, players)
        player_pos2 = self.controller.winner_table_position(winner2, players)
        player_pos3 = self.controller.winner_table_position(winner3, players)
        player_pos4 = self.controller.winner_table_position(winner4, players)

        assert player_pos1 == 0
        assert player_pos2 == 1
        assert player_pos3 == 2
        assert player_pos4 == 3

    def test_reset_players_cards_and_tricks_when_list_is_populated_returns_an_empty_list(self):
        player1, player2, player3, player4 = Player("George"), Player("Dan"), Player("Robert"), Player("Nicu")
        players = [player1, player2, player3, player4]

        player3.remove_cards.append("Ah")
        player3.remove_cards.append("Kh")
        self.controller.reset_players_cards_and_tricks(players)
        assert player3.remove_cards == []

    def test_update_score_when_tricks_are_completed_return_the_right_score(self):
        player1, player2, player3, player4 = Player("George"), Player("Dan"), Player("Robert"), Player("Nicu")
        players = [player1, player2, player3, player4]

        score1, score2 = 0, 0
        player1.tricks, player2.tricks, player3.tricks, player4.tricks = 4, 4, 2, 3
        scores = self.controller.update_score(score1, score2, players)
        assert scores == (0, 1)

    def test_update_score_when_tricks_are_completed_but_score_is_higher_than_one_return_the_right_score(self):
        player1, player2, player3, player4 = Player("George"), Player("Dan"), Player("Robert"), Player("Nicu")
        players = [player1, player2, player3, player4]

        score1, score2 = 0, 2
        player1.tricks, player2.tricks, player3.tricks, player4.tricks = 4, 4, 2, 3
        scores = self.controller.update_score(score1, score2, players)
        assert scores == (0, 3)
