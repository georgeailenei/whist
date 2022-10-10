import pytest
from whist.models import Player, GameStats
from whist.game_logic.services.controller import Controller
from whist.game_logic.domain.validate import ValidateCards
from whist.game_logic.domain.entity import Deck
from src.database_repository import GameData


@pytest.mark.django_db
class TestController:
    controller = Controller(ValidateCards(), GameData())

    def test_load_players_stats_from_db_when_loading_from_empty_db_returns_empty_lists_and_zeros(self):
        players_stats = self.controller.load_players_stats()

        assert players_stats['players_names'] == ["George", "Alex", "Dan", "Robert"]
        assert players_stats['players_cards'] == [[], [], [], []]
        assert players_stats['players_tricks'] == [0, 0, 0, 0]
        assert players_stats['removed_players_cards'] == [[], [], [], []]

    def test_load_players_stats_from_db_when_loading_from_populated_db_return_the_current_data_from_db(self):
        player1 = Player.objects.create(name="Alex", hand="Ah Kc 2c", tricks=0, played_cards="2c 3c")
        player2 = Player.objects.create(name="Gicu", hand="Ac 3c 5c", tricks=2, played_cards="Jh Jc")
        player3 = Player.objects.create(name="NeaCaiSa", hand="10h 7c 6c", tricks=1, played_cards="Qc Qh")
        player4 = Player.objects.create(name="Carlos", hand="2h 3h 4h", tricks=0, played_cards="8c 8h")

        players_stats = self.controller.load_players_stats()
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
        player1 = Player.objects.create(name="Alex", hand="Ah Kc 2c", tricks=0, played_cards="2c 3c")
        player2 = Player.objects.create(name="Gicu", hand="Ac 3c 5c", tricks=2, played_cards="Jh Jc")
        player3 = Player.objects.create(name="NeaCaiSa", hand="10h 7c 6c", tricks=1, played_cards="Qc Qh")
        player4 = Player.objects.create(name="Carlos", hand="2h 3h 4h", tricks=0, played_cards="8c 8h")

        players = self.controller.load_players()
        player_one, player_two, player_three, player_four = 0, 1, 2, 3

        assert players[player_one].name == "Alex"
        assert players[player_four].tricks == 0
        assert players[player_two].cards == ["Ac", "3c", "5c"]
        assert players[player_three].remove_cards == ["Qc", "Qh"]

    def test_load_game_stats_when_db_is_empty_returns_a_new_game(self):
        game_stats = self.controller.load_game_stats()
        assert game_stats["board"] == []
        assert game_stats["trump_card"] == "UNKNOWN"
        assert game_stats["score1"] == 0
        assert game_stats["score2"] == 0
        assert game_stats["player_pos"] == 0

    def test_load_game_stats_when_db_is_populated_returns_current_db_data(self):
        GameStats.objects.create(
            board="Ah Kc",
            trump_card="clubs",
            team_one_score=0,
            team_two_score=0,
            player_position=1
        )
        game_stats = self.controller.load_game_stats()
        assert game_stats["board"] == ["Ah", "Kc"]
        assert game_stats["trump_card"] == "clubs"
        assert game_stats["score1"] == 0
        assert game_stats["score2"] == 0
        assert game_stats["player_pos"] == 1

    def test_score_limit_when_score_is_below_five_returns_true(self):
        score_limit = self.controller.score_limit(4, 3)
        score_limit2 = self.controller.score_limit(0, 4)
        assert score_limit is True
        assert score_limit2 is True

    def test_score_limit_when_score_is_equal_or_above_five_returns_false(self):
        score_limit = self.controller.score_limit(5, 3)
        score_limit2 = self.controller.score_limit(7, 3)
        assert score_limit is False
        assert score_limit2 is False

    def test_players_cards_count_when_players_dont_have_cards_returns_zero(self):
        players = self.controller.load_players()
        total_cards = self.controller.players_cards_count(players)
        assert total_cards == 0

    def test_players_cards_count_when_players_have_cards_returns_total_count(self):
        player1 = Player.objects.create(name="Alex", hand="Ah, Kc, 2c", tricks=0, played_cards="2c, 3c")
        player2 = Player.objects.create(name="Gicu", hand="Ac, 3c, 5c", tricks=2, played_cards="Jh, Jc")
        player3 = Player.objects.create(name="NeaCaiSa", hand="10h, 7c, 6c", tricks=1, played_cards="Qc, Qh")
        player4 = Player.objects.create(name="Carlos", hand="2h, 3h, 4h", tricks=0, played_cards="8c, 8h")

        players = self.controller.load_players()
        total_cards = self.controller.players_cards_count(players)
        assert total_cards == 12

    def test_mix_cards_when_given_a_deck_of_cards_in_order_return_shuffled_deck(self):
        cards = Deck.cards
        shuffled_cards = self.controller.mix_cards(cards)
        another_shuffled = self.controller.mix_cards(cards)
        assert shuffled_cards != cards
        assert shuffled_cards != another_shuffled

    def test_get_shuffled_cards_when_asked_to_shuffle_again_returns_another_shuffled_deck(self):
        deck1 = self.controller.get_shuffled_cards()
        deck2 = self.controller.get_shuffled_cards()
        assert deck1 != deck2

    def test_spread_cards_when_players_have_no_cards_returns_13_cards_for_each_player(self):
        players = self.controller.load_players()
        cards = self.controller.get_shuffled_cards()
        players = self.controller.spread_cards(cards, players)
        player1, player2, player3, player4 = 0, 1, 2, 3

        assert len(players[player1].cards) == 13
        assert len(players[player2].cards) == 13
        assert len(players[player3].cards) == 13
        assert len(players[player4].cards) == 13

    def test_find_trump_card_when_cards_are_spread_returns_the_last_suit_from_deck(self):
        deck_example = ["Ah", "2c", "Jd"]
        deck_example2 = ["Ah", "2c", "Jc"]
        deck_example3 = ["Ah", "2c", "Jh"]
        deck_example4 = ["Ah", "2c", "Js"]

        trump_card1 = self.controller.find_trump_card(deck_example)
        trump_card2 = self.controller.find_trump_card(deck_example2)
        trump_card3 = self.controller.find_trump_card(deck_example3)
        trump_card4 = self.controller.find_trump_card(deck_example4)

        assert trump_card1 == "diamonds"
        assert trump_card2 == "clubs"
        assert trump_card3 == "hearts"
        assert trump_card4 == "spades"

    def test_total_tricks_completed_when_tricks_are_below_13_returns_true(self):
        players = self.controller.load_players()
        tricks_completed = self.controller.total_tricks_completed(players)
        assert tricks_completed is True

    def test_total_tricks_completed_when_tricks_are_equal_13_returns_false(self):
        player1 = Player.objects.create(name="Alex", hand="Ah, Kc, 2c", tricks=4, played_cards="2c, 3c")
        player2 = Player.objects.create(name="Gicu", hand="Ac, 3c, 5c", tricks=4, played_cards="Jh, Jc")
        player3 = Player.objects.create(name="NeaCaiSa", hand="10h, 7c, 6c", tricks=2, played_cards="Qc, Qh")
        player4 = Player.objects.create(name="Carlos", hand="2h, 3h, 4h", tricks=3, played_cards="8c, 8h")

        players = [player1, player2, player3, player4]
        tricks_completed = self.controller.total_tricks_completed(players)
        assert tricks_completed is False

    def test_card_rank_and_suit_when_the_card_is_ten_return_the_given_suit_and_rank(self):
        card1, card2, card3 = "10h", "10c", "Ac"
        assert self.controller.card_rank_and_suit(card1) == ["10", "h"]
        assert self.controller.card_rank_and_suit(card2) == ["10", "c"]
        assert self.controller.card_rank_and_suit(card3) == ["A", "c"]

    def test_get_card_rank_return_the_first_letter_unless_is_ten(self):
        card1, card2, card3, card4 = "2h", "Kd", "Ah", "10c"
        assert self.controller.get_card_rank(card1) == "2"
        assert self.controller.get_card_rank(card2) == "K"
        assert self.controller.get_card_rank(card3) == "A"
        assert self.controller.get_card_rank(card4) == "10"

    def test_get_card_suit_always_return_the_last_letter(self):
        card1, card2, card3, card4 = "2h", "Kd", "Ah", "10c"
        assert self.controller.get_card_suit(card1) == "h"
        assert self.controller.get_card_suit(card2) == "d"
        assert self.controller.get_card_suit(card3) == "h"
        assert self.controller.get_card_suit(card4) == "c"

    def test_add_to_board_when_receiving_new_card_return_the_list_of_cards_in_the_board(self):
        card1, card2, card3, card4 = "2h", "Kd", "Ah", "10c"
        board, board2, board3 = [], ["Ah"], ["Ad", "Ac"]
        assert self.controller.add_to_board(card1, board) == ["2h"]
        assert self.controller.add_to_board(card2, board2) == ["Ah", "Kd"]
        assert self.controller.add_to_board(card3, board3) == ["Ad", "Ac", "Ah"]
