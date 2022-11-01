from room.models import Stats


class GameData:
    def get_room_stats(self, room):
        stats = Stats.objects.all()
        all_room_stats = [room.room for room in stats]
        if room not in all_room_stats:
            return Stats.objects.create(room=room)
        elif room in all_room_stats:
            values = Stats.objects.filter(room=room).values()
            return Stats.objects.get(pk=values[0]['id'])

    def load_game_stats(self, room):
        room_stats = self.get_room_stats(room)
        players = room_stats.room.players.all()
        played_hands = [p.played_hand.split() for p in players]
        return {
                'board': room_stats.board,
                'trump_card': room_stats.trump_card,
                'score1': room_stats.team_one_score,
                'score2': room_stats.team_two_score,
                'player_pos': room_stats.player_position,
                'played_card': room_stats.played_card,
                'players': players,
                'removed_players_cards': played_hands,
                }

    def save_played_card(self, card, room_stats):
        room_stats.played_card = card
        room_stats.save()
