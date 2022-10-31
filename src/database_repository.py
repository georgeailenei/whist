from whist.models import Player, GameStats


class GameData:
    #
    # # PLAYER STATS
    # def save_player_stats(self, player_name, hand, tricks, played_cards):
    #     player = Player(
    #         name=player_name,
    #         hand=hand,
    #         tricks=tricks,
    #         played_cards=played_cards,
    #     )
    #     player.save()

    def get_all_players_stats(self):
        players = Player.objects.all()

        if len(players) == 0:
            return None
        else:
            players_names = [p.name for p in players]
            hands = [p.hand.split() for p in players]
            tricks = [p.tricks for p in players]
            played_cards = [p.played_cards.split() for p in players]

        return [players_names, hands, tricks, played_cards]

    def remove_all_players_stats(self):
        Player.objects.all().delete()

    def save_all_players_stats(self, names, hands, tricks, played_cards):
        self.remove_all_players_stats()
        for i in range(len(names)):
            self.save_player_stats(
                names[i],
                hands[i],
                tricks[i],
                played_cards[i]
            )

    # GAME STATS
    def get_game_stats(self):
        # The stats will remain on a single row for now.
        game_stats = GameStats.objects.all()

        if len(game_stats) == 0:
            return None
        else:
            game_stats = GameStats.objects.first()
            return [
                game_stats.board.split(),
                game_stats.trump_card,
                game_stats.team_one_score,
                game_stats.team_two_score,
                game_stats.player_position,
                game_stats.played_card
            ]

    def remove_game_stats(self):
        GameStats.objects.all().delete()

    def save_game_stats(self, board, trump_card, team_one_score, team_two_score, player_position, played_card):
        self.remove_game_stats()
        game_stats = GameStats.objects.create(
            board=board,
            trump_card=trump_card,
            team_one_score=team_one_score,
            team_two_score=team_two_score,
            player_position=player_position,
            played_card=played_card
        )
        game_stats.save()

    def save_played_card(self, card):
        game_stats = GameStats.objects.first()
        game_stats.played_card = card
        game_stats.save()
