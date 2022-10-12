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
        # Card Receiver
        form = GameForm()

        # Load Players & Game Stats
        players = self.controller.load_players()
        game_stats = self.controller.load_game_stats()

        # Game Stats
        board = game_stats['board']
        score_one = game_stats['score1']
        score_two = game_stats['score2']
        player_pos = game_stats['player_pos']

        current_player_pos = player_pos
        if current_player_pos == 4:
            current_player_pos = 0

        # Run Game
        if self.controller.score_limit(score_one, score_two):
            if self.controller.players_cards_count(players) == 0:
                cards = self.controller.get_shuffled_cards()
                players = self.controller.spread_cards(cards, players)
                game_stats['trump_card'] = self.controller.find_trump_card(cards)
                self.controller.save_players_stats(players)
                self.controller.save_game_stats(game_stats)

            elif self.controller.total_tricks_completed(players) is False:
                card = game_stats['played_card']
                trump_card = game_stats['trump_card']

                if card is not "":
                    the_card = self.controller.get_card(card)

                    if self.controller.correct_card(the_card, players, board, current_player_pos, trump_card):
                        board = self.controller.add_to_board(the_card, board)
                        players = self.controller.remove_card_from_player(the_card, players)
                        current_player_pos += 1

                        if self.controller.board_full(board):
                            winner_card = self.controller.compare_cards_rank(board, trump_card)
                            winner = self.controller.find_winner(winner_card, players)
                            players = self.controller.add_trick_to_player(winner, players)
                            current_player_pos = self.controller.winner_table_position(winner, players)
                            self.controller.clear_board(board)
                        # SAVE
                        self.controller.save_players_stats(players)
                        game_stats['board'] = board
                        game_stats['score1'] = score_one
                        game_stats['score2'] = score_two
                        game_stats['player_pos'] = current_player_pos
                        self.controller.save_game_stats(game_stats)

        if self.controller.total_tricks_completed(players) is True:
            scores = self.controller.update_score(score_one, score_one, players)
            self.controller.reset_players_cards_and_tricks(players)
            # SAVE
            self.controller.save_players_stats(players)
            game_stats['board'] = board
            game_stats['score1'] = scores[0]
            game_stats['score2'] = scores[1]
            game_stats['player_pos'] = current_player_pos
            self.controller.save_game_stats(game_stats)

            if self.controller.players_cards_count(players) == 0 and self.controller.score_limit(score_one, score_two):
                cards = self.controller.get_shuffled_cards()
                players = self.controller.spread_cards(cards, players)
                game_stats['trump_card'] = self.controller.find_trump_card(cards)
                self.controller.save_players_stats(players)
                self.controller.save_game_stats(game_stats)
            else:
                #  SHOW WINNER
                pass

        # RESULTS
        players = self.controller.load_players()
        game_stats = self.controller.load_game_stats()
        board = self.controller.display_board(game_stats['board'])
        trump_card = game_stats['trump_card']
        score_one = game_stats['score1']
        score_two = game_stats['score2']

        content = {
            # Form
            'form': form,

            # Players
            'player1': players[0],
            'player2': players[1],
            'player3': players[2],
            'player4': players[3],

            # GAME STATS
            'board': board,
            'trump_card': trump_card,
            'team_1_score': score_one,
            'team_2_score': score_two
        }
        return render(request, self.template_name, content)
