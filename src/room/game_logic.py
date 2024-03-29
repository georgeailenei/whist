from .entities import Deck, Card
from django.utils import timezone
import time


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
        elif team_one_score == 5 or team_two_score == 5:
            return False

    def players_cards_count(self, players):
        total = 0
        for player in players:
            total += len(player.hand)
        return total

    def spread_cards(self, cards, players):
        players[0].hand = cards[:13]
        players[1].hand = cards[13: 13 + 13]
        players[2].hand = cards[26: 26 + 13]
        players[3].hand = cards[39:]
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

        card_is_valid = self.card_validator.check_card(str(card))

        player_has_card = self.card_validator.check_players_cards(
            str(card), players[current_player].hand
        )
        player_played_right_suit = self.card_validator.check_right_suit(
            str(card),
            players[current_player].hand,
            first_card_suit,
            trump_card_suit,
        )
        if card_is_valid and player_has_card and player_played_right_suit:
            return True
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
            trump_cards = [
                index for index, suit in enumerate(suits) if suit == trump_card[0]
            ]
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
            first_suit_cards = [
                index for index, suit in enumerate(suits) if suit == first_suit
            ]
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
        winner = [
            player.username for player in players if winner_card in player.played_hand
        ]
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
        return [], board

    def update_score(self, team_one_score, team_two_score, players):
        team_one = [players[0].tricks, players[2].tricks]
        team_two = [players[1].tricks, players[3].tricks]
        team_one_score_result = sum(team_one)
        team_two_score_result = sum(team_two)

        if team_one_score_result > team_two_score_result:
            team_one_score += 1
        elif team_two_score_result > team_one_score_result:
            team_two_score += 1
        return [team_one_score, team_two_score]

    def reset_players_cards_and_tricks(self, players):
        for player in players:
            player.hand = ""
            player.tricks = 0
            player.played_hand = ""
            player.save()
        return players

    def play_card_for_player(self, card_room, room_stats, player):
        players = list(card_room.players.all())
        for card in player.hand.split():
            if self.correct_card(
                    card,
                    players,
                    room_stats.board.split(),
                    room_stats.player_position,
                    room_stats.trump_card,
            ):
                self.run(card_room, card, None, player.username)
                return

    def reset_room_stats(self, stats):
        stats.player_position = 0
        stats.team_one_score = 0
        stats.team_two_score = 0
        stats.players_choice = 0
        stats.cards_per_round = 0
        stats.save()
        return stats

    def game_first_hand(self, players):
        total_cards_in_play = 0
        for p in players:
            total_cards_in_play += len(p.hand.split())

        if total_cards_in_play == 52:
            return True
        else:
            return False

    def game_last_card(self, players):
        total_cards_in_play = 0
        for p in players:
            total_cards_in_play += len(p.hand.split())

        if total_cards_in_play == 1:
            for p in players:
                if len(p.hand.split()) == 1 and "Joker" not in p.hand.split():
                    p.hand += " Joker"

    def last_card(self, players):
        for p in players:
            if "Joker" in p.hand.split():
                return True

    def find_player_with_joker(self, players):
        for p in players:
            if "Joker" in p.hand.split():
                return p

    def cards_in_play(self, players):
        total_cards_in_play = 0
        for p in players:
            total_cards_in_play += len(p.hand.split())
        return total_cards_in_play

    def sort_players_cards(self, players):
        for p in players:
            p.hand = " ".join(str(e) for e in p.hand)
            p.choice = 0
            p.save()
        return players

    def setup_room(self, card_room, cards):
        stats = self.repository.get_room_stats(room=card_room)
        players = list(card_room.players.all())

        if len(players) == 4:
            players = self.spread_cards(cards, players)
            stats = self.reset_room_stats(stats)
            stats.trump_card = self.find_trump_card(cards)

            card_room.game_status = True
            card_room.save()
            stats.save()

            players = self.sort_players_cards(players)
            stats.cards_in_play = self.cards_in_play(players)
            stats.save()

    def player_leaves_or_stays(self, room, choice, player, players):
        if not choice and choice is not None:
            for p in players:
                if player == p.username and p.username not in room.leaving_players.split():
                    room.leaving_players = room.leaving_players + p.username + " "
                    p.choice = 1
                    p.save()

        if choice:
            for p in players:
                if player == p.username:
                    p.choice = 1
                    p.save()

    def game_ended_timeleft(self, room, room_stats, players):
        time_since_card_was_played = (timezone.now() - room_stats.last_played_card).total_seconds()

        if time_since_card_was_played > 6:
            room.game_status = False
            self.reset_players_cards_and_tricks(players)
            self.reset_room_stats(room_stats)

            for p in players:
                if p.choice == 0:
                    room.players.remove(p)
                elif p.choice == 1 and p.username in room.leaving_players.split():
                    room.players.remove(p)
        room.save()

    def run(self, room, played_card, choice, player):
        room_stats = self.repository.get_room_stats(room)
        room_stats.save()

        players = list(room.players.all())
        room_stats.cards_in_play = self.cards_in_play(players)

        board = room_stats.board.split()
        old_board = room_stats.old_board.split()

        game_ended = self.game_ended(room_stats.team_one_score, room_stats.team_two_score)
        one_set_is_finished = self.total_tricks_completed(players) is False
        is_correct_card = self.correct_card(
            played_card,
            players,
            board,
            room_stats.player_position,
            room_stats.trump_card,
        )

        # if room_stats.cards_in_play == 1:
        #     self.game_last_card(players)
        #     print(players[0].hand,
        #           players[1].hand,
        #           players[2].hand,
        #           players[3].hand)

        if game_ended and one_set_is_finished and is_correct_card:
            room_stats.last_played_card = timezone.now()
            room_stats.played_card = played_card
            board = self.add_to_board(played_card, board)

            room.stats.winner = ""
            room.stats.cards_per_round += 1
            if room.stats.cards_per_round == 5:
                room.stats.cards_per_round = 1

            players = self.remove_card_from_player(
                played_card, players
            )
            room_stats.player_position += 1
            if room_stats.player_position == 4:
                room_stats.player_position = 0

            if self.board_full(board):
                winner_card = self.compare_cards_rank(
                    board, room_stats.trump_card
                )
                winner = self.find_winner(winner_card, players)
                room.stats.winner = winner
                players = self.add_trick_to_player(winner, players)
                room_stats.player_position = self.winner_table_position(
                    winner, players
                )

                board, old_board = self.clear_board(board)
                room_stats.cards_in_play = self.cards_in_play(players)
                print(self.cards_in_play(players))

        # if "Joker" in players[room_stats.player_position]:
        #     players = self.remove_card_from_player(
        #         played_card, players
        #     )
        #
        # if self.last_card(players):
        #     self.run(room, "Joker", "", self.find_player_with_joker(players))
        #     room_stats.player_position = self.winner_table_position(
        #         self.find_player_with_joker(players), players
        #     )

        if self.total_tricks_completed(players):
            scores = self.update_score(
                room_stats.team_one_score, room_stats.team_two_score, players
            )
            room_stats.team_one_score = scores[0]
            room_stats.team_two_score = scores[1]

            # Reset Game
            self.reset_players_cards_and_tricks(players)
            cards = Deck().cards
            players = self.spread_cards(cards, players)
            room_stats.trump_card = self.find_trump_card(cards)
            self.sort_players_cards(players)

        if not game_ended:
            self.player_leaves_or_stays(room, choice, player, players)
            self.game_ended_timeleft(room, room_stats, players)

        self.repository.save_game_stats(room_stats, board, old_board)
