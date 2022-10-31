from room.models import Stats


class GameData:
    def load_game_stats(self, room):
        room_stats = Stats.objects.create(room=room)
        players = room_stats.room.players.all()
        names = [p.username for p in players]
        hands = [p.hand.split() for p in players]
        tricks = [p.tricks for p in players]
        played_hands = [p.played_hand.split() for p in players]
        return {
                'board': room_stats.board,
                'trump_card': room_stats.trump_card,
                'score1': room_stats.team_one_score,
                'score2': room_stats.team_two_score,
                'player_pos': room_stats.player_position,
                'played_card': room_stats.played_card,
                'players_names': names,
                'players_cards': hands,
                'players_tricks': tricks,
                'removed_players_cards': played_hands,
                }

    # def save_played_card(self, card):
    #     game_stats = GameStats.objects.first()
    #     game_stats.played_card = card
    #     game_stats.save()
