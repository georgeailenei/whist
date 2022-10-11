import random
from whist.game_logic.domain.entity import Player, Deck, Card


class Controller:
    def __init__(self, card_validator, repository):
        self.card_validator = card_validator
        self.repository = repository

    def load_players_stats(self):
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
        player_stats = self.load_players_stats()

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
        game_stats = self.repository.get_game_stats()
        board, trump_card, score1, score2, pos, played_card = 0, 1, 2, 3, 4, 5

        if game_stats is None:
            return {
                # START AN EMPTY GAME
                'board': [],
                'trump_card': "UNKNOWN",
                'score1': 0,
                'score2': 0,
                'player_pos': 0,
                'played_card': ""
            }
        else:
            board = [self.get_card(card) for card in game_stats[board]]
            return {
                'board': board,
                'trump_card': game_stats[trump_card],
                'score1': game_stats[score1],
                'score2': game_stats[score2],
                'player_pos': game_stats[pos],
                'played_card': game_stats[played_card]
            }

    # THIS METHOD IS NOT TESTED
    def display_board(self, board):
        the_board = [str(card) for card in board]
        return " ".join(the_board)

    def score_limit(self, team_one_score, team_two_score):
        if team_one_score < 5 and team_two_score < 5:
            return True
        elif team_one_score >= 5 or team_two_score >= 5:
            return False

    def players_cards_count(self, players):
        total = 0
        for player in players:
            total += len(player.cards)
        return total

    def mix_cards(self, cards):
        deck = cards.copy()
        random.shuffle(deck)
        return deck

    def get_shuffled_cards(self):
        return self.mix_cards(Deck.cards)

    def spread_cards(self, cards, players):
        i = 0
        for card in cards:
            if len(players[i].cards) != 13:
                players[i].cards.append(card)
            else:
                i += 1
                players[i].cards.append(card)
        return players

    def find_trump_card(self, cards):
        suits = {"hearts": "h", "clubs": "c", "diamonds": "d", "spades": "s"}
        last_suit = cards[-1][-1]

        for suit_name, suit_abv in suits.items():
            if last_suit == suit_abv:
                return suit_name

    # Save players stats and save game stats must be tested before moving forward;
    def save_players_stats(self, players):
        names = [p.name for p in players]
        hands = [" ".join(p.cards) for p in players]
        tricks = [p.tricks for p in players]
        played_cards = [" ".join(p.remove_cards) for p in players]
        self.repository.save_all_players_stats(names, hands, tricks, played_cards)

    def save_game_stats(self, game_stats):
        board = " ".join(str(card) for card in game_stats['board'])
        trump_card = game_stats['trump_card']
        team_one_score = game_stats['score1']
        team_two_score = game_stats['score2']
        player_position = game_stats['player_pos']
        played_card = game_stats['played_card']
        self.repository.save_game_stats(board, trump_card, team_one_score, team_two_score, player_position, played_card)

    def total_tricks_completed(self, players):
        all_tricks = [player.tricks for player in players]
        if sum(all_tricks) != 13:
            return True
        elif sum(all_tricks) == 13:
            return False

    def save_card(self, card):
        self.repository.save_played_card(card)

    def card_rank_and_suit(self, card):
        if len(card) == 3:
            return ["10", card[-1]]
        return list(card)

    def get_card_rank(self, card):
        card_properties = self.card_rank_and_suit(card)
        return card_properties[0]

    def get_card_suit(self, card):
        card_properties = self.card_rank_and_suit(card)
        return card_properties[1]

    def get_card(self, card):
        card_rank = self.get_card_rank(card)
        card_suit = self.get_card_suit(card)
        return Card(card_rank, card_suit)

    def correct_card(self, card, players, board, current_player, trump_card):
        first_card_suit = None
        trump_card_suit = trump_card[0]

        if len(board) > 0:
            first_card_suit = board[0].suit

        if self.card_validator.check_card(str(card)):
            if self.card_validator.check_players_cards(str(card), players[current_player].cards):
                if self.card_validator.check_right_suit(str(card), players[current_player].cards, first_card_suit, trump_card_suit):
                    return True
                else:
                    return False

    def add_to_board(self, card, board):
        current_board = board
        current_board.append(card)
        return current_board

    def remove_card_from_player(self, card, players):
        for player in players:
            if str(card) in player.cards:
                player.remove_cards.append(str(card))
                player.cards.remove(str(card))
        return players

    def board_full(self, board):
        if len(board) == 4:
            return True
        elif len(board) < 4:
            return False

    def find_winner(self, winner_card, players):
        winner = [player.name for player in players if winner_card in player.remove_cards]
        return winner[0]

    def add_trick_to_player(self, winner, players):
        for player in players:
            if player.name == winner:
                player.tricks += 1
        return players

    def winner_table_position(self, winner, players):
        current_players_name = [player.name for player in players]
        return current_players_name.index(winner)

    # THIS METHOD IS NOT TESTED
    def clear_board(self, board):
        new_board = board.clear()
        return new_board

    # def reset_players_cards_and_tricks(self, players):
    #     for player in players:
    #         player.tricks = 0
    #         player.cards.clear()
    #     return players
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

    def compare_cards_rank(self, board, trump_card):
        suits = [card.suit for card in board]
        ranks = [str(card.rank) for card in board]
        J, Q, K, A = 11, 12, 13, 14
        winner_card = 0
        compare = 0
        first_suit = str(board[0].suit)

        if trump_card[0] in suits:
            trump_cards = [index for index, suit in enumerate(suits) if suit == trump_card[0]]
            if len(trump_cards) == 1:
                winner_card = str(board[trump_cards[0]])
                return winner_card

            elif len(trump_cards) > 1:
                for card in trump_cards:
                    if ranks[card] == "J":
                        compare = J
                        if compare > winner_card:
                            winner_card = compare
                    elif ranks[card] == "Q":
                        compare = Q
                        if compare > winner_card:
                            winner_card = compare
                    elif ranks[card] == "K":
                        compare = K
                        if compare > winner_card:
                            winner_card = compare
                    elif ranks[card] == "A":
                        compare = A
                        if compare > winner_card:
                            winner_card = compare
                    elif int(ranks[card]) > winner_card:
                        winner_card = int(ranks[card])

                if winner_card == 11:
                    winner_card = f"J{trump_card[0]}"
                elif winner_card == 12:
                    winner_card = f"Q{trump_card[0]}"
                elif winner_card == 13:
                    winner_card = f"K{trump_card[0]}"
                elif winner_card == 14:
                    winner_card = f"A{trump_card[0]}"
                else:
                    winner_card = f"{winner_card}{trump_card[0]}"
                return winner_card

        elif suits.count(first_suit) == 1:
            winner_card = str(board[0])
            return winner_card

        elif suits.count(first_suit) > 1:
            first_suit_cards = [index for index, suit in enumerate(suits) if suit == first_suit]
            for card in first_suit_cards:
                if ranks[card] == "J":
                    compare = J
                    if compare > winner_card:
                        winner_card = compare
                elif ranks[card] == "Q":
                    compare = Q
                    if compare > winner_card:
                        winner_card = compare
                elif ranks[card] == "K":
                    compare = K
                    if compare > winner_card:
                        winner_card = compare
                elif ranks[card] == "A":
                    compare = A
                    if compare > winner_card:
                        winner_card = compare
                elif int(ranks[card]) > winner_card:
                    winner_card = int(ranks[card])

            if winner_card == 11:
                winner_card = f"J{first_suit}"
            elif winner_card == 12:
                winner_card = f"Q{first_suit}"
            elif winner_card == 13:
                winner_card = f"K{first_suit}"
            elif winner_card == 14:
                winner_card = f"A{first_suit}"
            else:
                winner_card = f"{winner_card}{first_suit}"
            return winner_card

