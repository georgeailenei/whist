import random
from whist.game_logic.domain.entity import Player


class Controller:
    def __init__(self, card_validator, repository):
        self.card_validator = card_validator
        self.repository = repository

    def load_players_stats_from_db(self):
        players = self.repository.get_all_players_stats()
        names, hands, tricks, played_hands = 0, 1, 2, 3

        if players is None:
            return {
                # These players are just an example
                'players_names': ["George", "Alex", "Dan", "Robert"],
                'players_cards': [[], [], [], []],
                'players_tricks': [0, 0, 0, 0],
                'removed_players_cards': [[], [], [], []],
            }
        else:
            return {
                'players_names': players[names],
                'players_cards': players[hands],
                'players_tricks': players[tricks],
                'removed_players_cards': players[played_hands],
            }

    def load_players(self):
        player_stats = self.load_players_stats_from_db()

        # Players OBJ
        names = player_stats['players_names']
        players = [Player(names[0]), Player(names[1]), Player(names[2]), Player(names[3])]

        # Players Stats
        current_cards = player_stats['players_cards']
        current_tricks = player_stats['players_tricks']
        removed_cards = player_stats['removed_players_cards']

        for i in range(len(players)):
            players[i].cards = current_cards[i]
            players[i].tricks = current_tricks[i]
            players[i].remove_cards = removed_cards[i]
        return players

    def load_game_stats(self):
        pass

    # def save_game(self, players, board, score_one, score_two, trump_card):
    #     player1, player2, player3, player4 = 0, 1, 2, 3
    #
    #     players_names = [players[player1].name, players[player2].name, players[player3].name, players[player4].name]
    #     players_cards = [players[player1].cards, players[player2].cards, players[player3].cards, players[player4].cards]
    #     players_tricks = [players[player1].tricks, players[player2].tricks, players[player3].tricks,
    #                       players[player4].tricks]
    #     players_removed_cards = [players[player1].remove_cards, players[player2].remove_cards,
    #                              players[player3].remove_cards, players[player4].remove_cards]
    #
    #     self.repository.save_all(players_names, players_cards, players_tricks, board, score_one, score_two, trump_card,
    #                              players_removed_cards)

    # def save_card(self, card):
    #     self.repository.save_played_card(card)
    #
    # def get_card(self):
    #     return self.repository.get_played_card()
    #
    # def save_player_pos(self, current_position):
    #     self.repository.save_player_pos(current_position)
    #
    # def get_player_pos(self):
    #     return int(self.repository.get_player_pos())
    #
    # def card_rank_and_suit(self, card):
    #     if len(card) == 3:
    #         return [10, card[-1]]
    #     return list(card)
    #
    # def get_card_rank(self, card):
    #     card_properties = self.card_rank_and_suit(card)
    #     return card_properties[0]
    #
    # def get_card_suit(self, card):
    #     card_properties = self.card_rank_and_suit(card)
    #     return card_properties[1]
    #
    # def mix_cards(self, cards):
    #     deck = cards.copy()
    #     random.shuffle(deck)
    #     return deck
    #
    # def spread_cards(self, cards, players):
    #     i = 0
    #     for card in cards:
    #         if len(players[i].cards) != 13:
    #             players[i].cards.append(card)
    #         else:
    #             i += 1
    #             players[i].cards.append(card)
    #     return players
    #
    # def find_trump_card(self, cards):
    #     suits = {"hearts": "h", "clubs": "c", "diamonds": "d", "spades": "s"}
    #     last_suit = cards[-1][-1]
    #
    #     for suit_name, suit_abv in suits.items():
    #         if last_suit == suit_abv:
    #             return suit_name
    #
    # def reset_players_cards_and_tricks(self, players):
    #     for player in players:
    #         player.tricks = 0
    #         player.cards.clear()
    #     return players
    #
    # def correct_card(self, card:object, players:list, board:list, current_player: int, trump_card):
    #     first_card_suit = None
    #     trump_card_suit = trump_card[0]
    #
    #     if len(board) > 0:
    #         first_card_suit = board[0].suit
    #
    #     if self.card_validator.check_card(str(card)):
    #         if self.card_validator.check_players_cards(str(card), players[current_player].cards):
    #             if self.card_validator.check_right_suit(str(card), players[current_player].cards, first_card_suit, trump_card_suit):
    #                 return True
    #             else:
    #                 return False
    #
    # def add_to_board(self, card, board):
    #     current_board = board
    #     current_board.append(card)
    #
    # def winner_table_position(self, winner, players):
    #     current_players_name = [player.name for player in players]
    #     return current_players_name.index(winner)
    #
    # def add_trick_to_player(self, winner, players):
    #     for player in players:
    #         if player.name == winner.name:
    #             player.tricks += 1
    #     return players
    #
    # def find_winner(self, winner_card, players):
    #     winner = [player.name for player in players if winner_card in player.remove_cards]
    #     return winner[0]
    #
    # def remove_card_from_player(self, card, players):
    #     for player in players:
    #         if str(card) in player.cards:
    #             player.remove_cards.append(str(card))
    #             player.cards.remove(str(card))
    #     return players
    #
    # # if the board contains 4 cards, return TRUE;
    # def board_full(self, board):
    #     if len(board) == 4:
    #         return True
    #
    # def clear_board(self, board):
    #     return board.clear()
    #
    # def update_score(self, team_one_score, team_two_score, players):
    #     team_one = [players[0].tricks, players[2].tricks]
    #     team_two = [players[1].tricks, players[3].tricks]
    #     team_one_score_result = sum(team_one) - 6
    #     team_two_score_result = sum(team_two) - 6
    #
    #     if team_one_score_result > 0:
    #         team_one_score = team_one_score_result
    #     elif team_two_score_result > 0:
    #         team_two_score = team_two_score_result
    #     return team_one_score, team_two_score
    #
    # def score_limit(self, team_one_score, team_two_score):
    #     if team_one_score != 5 or team_two_score != 5:
    #         return True
    #
    # def total_tricks_completed(self, players):
    #     all_tricks = [player.tricks for player in players]
    #     if sum(all_tricks) != 13:
    #         return True
    #
    # def players_hand(self, players):
    #     total = 0
    #     for player in players:
    #         total += len(player.cards)
    #     return total
    #
    # def compare_cards_rank(self, board, trump_card):
    #     suits = [card.suit for card in board]
    #     ranks = [str(card.rank) for card in board]
    #     J, Q, K, A = 11, 12, 13, 14
    #     winner_card = 0
    #     compare = 0
    #     first_suit = str(board[0].suit)
    #
    #     if trump_card[0] in suits:
    #         trump_cards = [index for index, suit in enumerate(suits) if suit == trump_card[0]]
    #         if len(trump_cards) == 1:
    #             winner_card = str(board[trump_cards[0]])
    #             return winner_card
    #
    #         elif len(trump_cards) > 1:
    #             for card in trump_cards:
    #                 if ranks[card] == "J":
    #                     compare = J
    #                     if compare > winner_card:
    #                         winner_card = compare
    #                 elif ranks[card] == "Q":
    #                     compare = Q
    #                     if compare > winner_card:
    #                         winner_card = compare
    #                 elif ranks[card] == "K":
    #                     compare = K
    #                     if compare > winner_card:
    #                         winner_card = compare
    #                 elif ranks[card] == "A":
    #                     compare = A
    #                     if compare > winner_card:
    #                         winner_card = compare
    #                 elif int(ranks[card]) > winner_card:
    #                     winner_card = int(ranks[card])
    #
    #             if winner_card == 11:
    #                 winner_card = f"J{trump_card[0]}"
    #             elif winner_card == 12:
    #                 winner_card = f"Q{trump_card[0]}"
    #             elif winner_card == 13:
    #                 winner_card = f"K{trump_card[0]}"
    #             elif winner_card == 14:
    #                 winner_card = f"A{trump_card[0]}"
    #             else:
    #                 winner_card = f"{winner_card}{trump_card[0]}"
    #             return winner_card
    #
    #     elif suits.count(first_suit) == 1:
    #         winner_card = str(board[0])
    #         return winner_card
    #
    #     elif suits.count(first_suit) > 1:
    #         first_suit_cards = [index for index, suit in enumerate(suits) if suit == first_suit]
    #         for card in first_suit_cards:
    #             if ranks[card] == "J":
    #                 compare = J
    #                 if compare > winner_card:
    #                     winner_card = compare
    #             elif ranks[card] == "Q":
    #                 compare = Q
    #                 if compare > winner_card:
    #                     winner_card = compare
    #             elif ranks[card] == "K":
    #                 compare = K
    #                 if compare > winner_card:
    #                     winner_card = compare
    #             elif ranks[card] == "A":
    #                 compare = A
    #                 if compare > winner_card:
    #                     winner_card = compare
    #             elif int(ranks[card]) > winner_card:
    #                 winner_card = int(ranks[card])
    #
    #         if winner_card == 11:
    #             winner_card = f"J{first_suit}"
    #         elif winner_card == 12:
    #             winner_card = f"Q{first_suit}"
    #         elif winner_card == 13:
    #             winner_card = f"K{first_suit}"
    #         elif winner_card == 14:
    #             winner_card = f"A{first_suit}"
    #         else:
    #             winner_card = f"{winner_card}{first_suit}"
    #         return winner_card
    #
