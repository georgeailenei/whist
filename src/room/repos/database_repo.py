from room.models import Stats


class GameData:
    def get_room_stats(self, room):
        if hasattr(room, "stats") is False:
            return Stats.objects.create(room=room)
        else:
            return room.stats

    def convert_board(self, board):
        return " ".join(str(card) for card in board)

    def save_game_stats(self, room_stats, board, old_board):
        players = room_stats.room.players.all()
        room_stats.board = self.convert_board(board)
        room_stats.old_board = self.convert_board(old_board)

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
