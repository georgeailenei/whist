from room.models import Stats


class GameData:
    def get_room_stats(self, room):
        stats = Stats.objects.all()
        all_room_stats = [room.room for room in stats]

        if room not in all_room_stats:
            room_stats = Stats.objects.create(room=room)
        else:
            room_stats = Stats.objects.all().filter(room=room)

        return room_stats

    def load_game_stats(self, room):
        room_stats = self.get_room_stats(room)
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

    def save_played_card(self, card, room):
        room_stats = self.get_room_stats(room)
        room_stats.played_card = card
        room_stats.save()
