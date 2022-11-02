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

    def save_game_stats(self,
                        room, board, trump_card, team_one_score, team_two_score,
                        player_position, played_card, hands, tricks, played_cards
                        ):
        self.remove_all_stats(room)
        room_stats = self.get_room_stats(room)
        players = room_stats.room.players.all()
        room_stats.board = board
        room_stats.trump_card = trump_card
        room_stats.team_one_score = team_one_score
        room_stats.team_two_score = team_two_score
        room_stats.player_position = player_position
        room_stats.played_card = played_card

        i = 0
        for player in players:
            player.hand = hands[i]
            player.tricks = tricks[i]
            player.played_hand = played_cards[i]
            player.save()
            i += 1

        room_stats.save()

    def save_played_card(self, card, room):
        room = self.get_room_stats(room)
        room.played_card = card
        room.save()

    def remove_all_stats(self, room):
        room_stats = self.get_room_stats(room)
        players = room_stats.room.players.all()

        for player in players:
            player.hand = ""
            player.tricks = 0
            player.played_hand = ""

        room_stats.board = ""
        room_stats.trump_card = ""
        room_stats.team_one_score = 0
        room_stats.team_two_score = 0
        room_stats.player_position = 0
        room_stats.played_card = ""
        room_stats.save()

