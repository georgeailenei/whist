

class GameController:
    def __init__(self, card_validator, repository):
        self.card_validator = card_validator
        self.repository = repository

    def load_game(self, room):
        content = self.repository.load_game_stats(room)
        return {
            'board': content['board'],
            'trump_card': content['trump_card'],
            'score1': content['score1'],
            'score2': content['score2'],
            'player_pos': content['player_pos'],
            'played_card': content['played_card'],
            'players': content['players'],
            'removed_players_cards': content['removed_players_cards'],
        }

    def check_card(self, card):
        return self.card_validator.check_card(card)

    def save_card(self, card, room):
        self.repository.save_played_card(card, room)

    def run(self, form, room):
        game_stats = self.load_game(room)

        # Game Stats
        players = game_stats['players']
        board = game_stats['board']
        score_one = game_stats['score1']
        score_two = game_stats['score2']
        player_pos = game_stats['player_pos']

        current_player_pos = player_pos
        if current_player_pos == 4:
            current_player_pos = 0
        #
        # # run
        # if self.score_limit(score_one, score_two):
        #     if self.players_cards_count(players) == 0:
        #         cards = self.get_shuffled_cards()
        #         players = self.spread_cards(cards, players)
        #         game_stats['trump_card'] = self.find_trump_card(cards)
        #         self.save_players_stats(players)
        #         self.save_game_stats(game_stats)
        #
        #     elif self.total_tricks_completed(players) is False:
        #         card = game_stats['played_card']
        #         trump_card = game_stats['trump_card']
        #
        #         if card is not "":
        #             the_card = self.get_card(card)
        #
        #             if self.correct_card(the_card, players, board, current_player_pos, trump_card):
        #                 board = self.add_to_board(the_card, board)
        #                 players = self.remove_card_from_player(the_card, players)
        #                 current_player_pos += 1
        #
        #                 if self.board_full(board):
        #                     winner_card = self.compare_cards_rank(board, trump_card)
        #                     winner = self.find_winner(winner_card, players)
        #                     players = self.add_trick_to_player(winner, players)
        #                     current_player_pos = self.winner_table_position(winner, players)
        #                     self.clear_board(board)
        #                 # SAVE
        #                 self.save_players_stats(players)
        #                 game_stats['board'] = board
        #                 game_stats['score1'] = score_one
        #                 game_stats['score2'] = score_two
        #                 game_stats['player_pos'] = current_player_pos
        #                 self.save_game_stats(game_stats)
        #
        # if self.total_tricks_completed(players) is True:
        #     scores = self.update_score(score_one, score_one, players)
        #     self.reset_players_cards_and_tricks(players)
        #     # SAVE
        #     self.save_players_stats(players)
        #     game_stats['board'] = board
        #     game_stats['score1'] = scores[0]
        #     game_stats['score2'] = scores[1]
        #     game_stats['player_pos'] = current_player_pos
        #     self.save_game_stats(game_stats)
        #
        #     if self.players_cards_count(players) == 0 and self.score_limit(score_one, score_two):
        #         cards = self.get_shuffled_cards()
        #         players = self.spread_cards(cards, players)
        #         game_stats['trump_card'] = self.find_trump_card(cards)
        #         self.save_players_stats(players)
        #         self.save_game_stats(game_stats)
        #     else:
        #         #  SHOW WINNER
        #         pass
        #
        # # RESULTS
        # players = self.load_players()
        # game_stats = self.load_game_stats()
        # board = self.display_board(game_stats['board'])
        # trump_card = game_stats['trump_card']
        # score_one = game_stats['score1']
        # score_two = game_stats['score2']

        content = {
            'form': form,
            # Players
            'player1': players[0],
            'player2': players[1],
            'player3': players[2],
            'player4': players[3],

            # GAME STATS
            'board': board,
            # 'trump_card': trump_card,
            'team_1_score': score_one,
            'team_2_score': score_two,

            # HTML ELEMENTS
            'table_status': False,
            'game_status': True,
            'register': False,
            'cancel': False,
            'countdown': False,
            'timer': "0",
        }
        return content

