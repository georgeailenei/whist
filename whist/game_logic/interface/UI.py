from domain.entity import Deck, Player, Board, Card, Score
import os


class UI:
    game_title = "WHIST"
    ready_text = "Ready to play? "
    name_text = "Choose a name"
    deal_text = "Deal Cards"

    def __init__(self, controller):
        self.controller = controller

    def display_game_title(self):
        print(self.game_title)

    def display_game_option(self, text):
        while True:
            option = input(text)
            if option == "":
                return True

    def display_players(self, players):
        for player in players:
            print(str(player))

    def collect_players_names(self):
        player_one = input(self.name_text + ", player_one: ")
        player_two = input(self.name_text + ", player_two: ")
        player_three = input(self.name_text + ", player_three: ")
        player_four = input(self.name_text + ", player_four: ")
        return [Player(player_one), Player(player_two), Player(player_three), Player(player_four)]

    def mixed_cards(self):
        cards = Deck().cards
        return self.controller.mix_cards(cards)

    def the_trump_card(self, cards):
        return self.controller.find_trump_card(cards)

    def collect_card(self, player):
        while True:
            card = input(f"Choose a card, {player}: ")
            if self.controller.card_validator.check_card(card):
                card_properties = self.controller.card_rank_and_suit(card)
                rank, suit = card_properties[0], card_properties[1]
                return Card(rank, suit)

    def display_board(self, board):
        for card in board:
            print(card)

    def run(self):
        self.display_game_title()
        if self.display_game_option(self.ready_text):
            os.system("cls")
            players = self.collect_players_names()
            team_one_score = Score().score
            team_two_score = Score().score

            while self.controller.score_limit(team_one_score, team_two_score):
                if self.display_game_option(self.deal_text):
                    os.system("cls")
                    team_one_score, team_two_score = self.controller.update_score(team_one_score, team_two_score, players)
                    print(f"Current score: Team 1: {team_one_score} - Team 2: {team_two_score}")

                    self.controller.reset_players_cards_and_tricks(players)
                    cards = self.mixed_cards()
                    players = self.controller.spread_cards(cards, players)

                    self.display_players(players)
                    trump_card = self.the_trump_card(cards)
                    print(f"The trump cards are: {trump_card}")

                    board = Board().board
                    current_player_pos = 0
                    while self.controller.total_tricks_completed(players):
                        if current_player_pos == len(players):
                            current_player_pos = 0

                        card = self.collect_card(players[current_player_pos].name)

                        if self.controller.correct_card(card, players, board, current_player_pos, trump_card):
                            self.controller.add_to_board(card, board)
                            self.controller.remove_card_from_player(card, players)
                            self.display_board(board)
                            current_player_pos += 1

                        if self.controller.board_full(board, players):
                            winner_card = self.controller.compare_cards_rank(board, trump_card)
                            winner = self.controller.find_winner(winner_card, players)
                            print(f"Player {winner} with {winner_card} wins this trick")

                            self.controller.add_trick_to_player(winner, players)
                            current_player_pos = self.controller.winner_table_position(winner, players)
                            self.controller.clear_board(board)
                            self.display_players(players)
