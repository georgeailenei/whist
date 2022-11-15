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

    def convert_board(self, board):
        return " ".join(str(card) for card in board)

    def save_game_stats(self, room_stats, board):
        players = room_stats.room.players.all()
        room_stats.board = self.convert_board(board)

        hands = [p.hand for p in players]
        tricks = [p.tricks for p in players]
        played_cards = [p.played_hand for p in players]

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
