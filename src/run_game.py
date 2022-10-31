def run(self, form):
    # Load Players & Game Stats
    players = self.load_players()
    game_stats = self.load_game_stats()

    # Game Stats
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
        'team_2_score': score_two
    }
    return content
