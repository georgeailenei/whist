

class Controller:
    def check_user(self, user, card_room):
        players = card_room.players.all()
        return user not in players

    def add_player(self, user, card_room):
        if not self.check_user(user, card_room):
            raise ValueError('You are registered!')
        card_room.players.add(user)

    def numbers_of_players_waiting(self, card_room):
        players = card_room.players.all()
        return len(players)
