from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from whist.forms import GameForm
from whist.utils import get_controller


class GamesView(TemplateView):
    template_name = 'whist/games.html'


class WhistView(TemplateView):
    template_name = 'whist/whist.html'

    def __init__(self):
        super().__init__()
        self.controller = get_controller()

    def post(self, request):
        form = GameForm(request.POST)
        if form.is_valid():
            card = form.cleaned_data['input']

            if self.controller.card_validator.check_card(card):
                self.controller.save_card(card)

            form = GameForm()
            return redirect('whist')

    def get(self, request):
        form = GameForm()
        players = self.controller.load_players()
        # game_stats = self.controller.load_game_stats()

        # # Board OBJ
        # current_board = game['board']
        # board = []
        #
        # for card in current_board:
        #     board.append(Card(self.controller.get_card_rank(card), self.controller.get_card_suit(card)))
        #
        # # The Score
        # scores = game['scores']
        # score_one = scores[0]
        # score_two = scores[1]
        #
        # # Player position & reset if it goes above 3;
        # current_player_pos = self.controller.get_player_pos()
        # if current_player_pos == 4:
        #     current_player_pos = 0
        #
        # if self.controller.score_limit(score_one, score_two):
        #     if self.controller.players_hand(players) == 0:
        #         cards = self.controller.mix_cards(Deck.cards)
        #         players = self.controller.spread_cards(cards, players)
        #         trump_card = self.controller.find_trump_card(cards)
        #         self.controller.save_game(players, board, score_one, score_two, trump_card)
        #
        #     elif self.controller.total_tricks_completed(players):
        #         card = self.controller.get_card()
        #         trump_card = game['trump_card']
        #
        #         if card is not None:
        #             the_card = Card(self.controller.get_card_rank(card), self.controller.get_card_suit(card))
        #
        #             if self.controller.correct_card(the_card, players, board, current_player_pos, trump_card):
        #                 self.controller.add_to_board(the_card, board)
        #                 self.controller.remove_card_from_player(the_card, players)
        #                 current_player_pos += 1
        #
        #                 if self.controller.board_full(board):
        #                     winner_card = self.controller.compare_cards_rank(board, trump_card)
        #                     winner = self.controller.find_winner(winner_card, players)
        #                     self.controller.add_trick_to_player(winner, players)
        #                     current_player_pos = self.controller.winner_table_position(winner, players)
        #                     self.controller.clear_board(board)
        #
        #         # save player pos and game
        #         self.controller.save_player_pos(current_player_pos)
        #         self.controller.save_game(players, board, score_one, score_two, trump_card)
        #
        #     game_results = self.controller.load_game()
        #     current_board = game_results['board']
        #     trump_card = game_results['trump_card']

        content = {

            # Form
            'form': form,

            # Players
            'player1': players[0],
            'player2': players[1],
            'player3': players[2],
            'player4': players[3],

            # # Board & Trump Card
            # 'board': current_board,
            # 'trump_card': trump_card,
            #
            # # The Score
            # 'team_1_score': score_one,
            # 'team_2_score': score_two
        }

        return render(request, self.template_name, content)
