from .entities import Deck, Card


class GameController:
    def __init__(self, card_validator, repository):
        self.card_validator = card_validator
        self.repository = repository

    def check_card(self, card):
        return self.card_validator.check_card(card)

    def save_card(self, card, room):
        self.repository.save_played_card(card, room)

    def game_ended(self, team_one_score, team_two_score):
        if team_one_score < 5 and team_two_score < 5:
            return True
        elif team_one_score >= 5 or team_two_score >= 5:
            return False

    def players_cards_count(self, players):
        total = 0
        for player in players:
            total += len(player.hand)
        return total

    def spread_cards(self, cards, players):
        i = 0
        hands = [[], [], [], []]
        for card in cards:
            if len(hands[i]) != 13:
                hands[i].append(card)
                players[i].hand = hands[i]
            else:
                i += 1
                hands[i].append(card)
                players[i].hand = hands[i]
        return players

    def find_trump_card(self, cards):
        suits = {"hearts": "h", "clubs": "c", "diamonds": "d", "spades": "s"}
        last_suit = cards[-1][-1]

        for suit_name, suit_abv in suits.items():
            if last_suit == suit_abv:
                return suit_name

    def total_tricks_completed(self, players):
        all_tricks = [player.tricks for player in players]
        if sum(all_tricks) != 13:
            return False
        elif sum(all_tricks) == 13:
            return True

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
            first_card_suit = board[0][-1]

        if self.card_validator.check_card(str(card)):
            if self.card_validator.check_players_cards(str(card), players[current_player].hand):
                if self.card_validator.check_right_suit(str(card), players[current_player].hand, first_card_suit, trump_card_suit):
                    return True
                else:
                    return False

    def add_to_board(self, card, board):
        board.append(card)
        return board

    def remove_card_from_player(self, card, players):
        for player in players:
            if str(card) in player.hand:
                player.played_hand += " " + str(card)
                player.hand = player.hand.replace(str(card), "")
                player.save()
        return players

    def board_full(self, board):
        if len(board) == 4:
            return True
        elif len(board) < 4:
            return False

    def compare_cards_rank(self, board, trump_card):
        cards = [self.get_card(card) for card in board]
        suits = [card.suit for card in cards]
        ranks = [str(card.rank) for card in cards]
        J, Q, K, A = 11, 12, 13, 14
        winner_card = 0
        compare = 0
        first_suit = board[0][-1]

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

    def find_winner(self, winner_card, players):
        winner = [player.username for player in players if winner_card in player.played_hand]
        return winner[0]

    def add_trick_to_player(self, winner, players):
        for player in players:
            if player.username == winner:
                player.tricks += 1
                player.save()
        return players

    def winner_table_position(self, winner, players):
        current_players_name = [player.username for player in players]
        return current_players_name.index(winner)

    def clear_board(self, board):
        return board.clear()

    def update_score(self, team_one_score, team_two_score, players):
        team_one = [players[0].tricks, players[2].tricks]
        team_two = [players[1].tricks, players[3].tricks]
        team_one_score_result = sum(team_one) - 6
        team_two_score_result = sum(team_two) - 6

        if team_one_score_result > 0:
            team_one_score += team_one_score_result
        elif team_two_score_result > 0:
            team_two_score += team_two_score_result
        return team_one_score, team_two_score

    def reset_players_cards_and_tricks(self, players):
        for player in players:
            player.hand = ""
            player.tricks = 0
            player.played_hand = ""
            player.save()
        return players

    def run(self, room, played_card):
        room_stats = self.repository.get_room_stats(room)
        room_stats.played_card = played_card
        room_stats.save()
        players = list(room.players.all())
        board = room_stats.board.split()

        if room_stats.player_position == 4:
            room_stats.player_position = 0

        if self.game_ended(room_stats.team_one_score, room_stats.team_two_score):
            one_set_is_finished = self.total_tricks_completed(players) is False

            if one_set_is_finished:
                if self.correct_card(room_stats.played_card, players, board, room_stats.player_position, room_stats.trump_card):
                    board = self.add_to_board(room_stats.played_card, board)
                    players = self.remove_card_from_player(room_stats.played_card, players)
                    room_stats.player_position += 1

                    if self.board_full(board):
                        winner_card = self.compare_cards_rank(board, room_stats.trump_card)
                        winner = self.find_winner(winner_card, players)
                        players = self.add_trick_to_player(winner, players)
                        room_stats.player_position = self.winner_table_position(winner, players)
                        self.clear_board(board)

        if self.total_tricks_completed(players):
            scores = self.update_score(room_stats.team_one_score, room_stats.team_one_score, players)
            self.reset_players_cards_and_tricks(players)

            room_stats.team_one_score = scores[0]
            room_stats.team_two_score = scores[1]

        # RESULTS
        self.repository.save_game_stats(room_stats, board)
