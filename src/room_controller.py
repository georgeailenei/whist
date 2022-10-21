

class Controller:
    def check_user(self, user, card_room):
        players = card_room.players.all()
        return user not in players

    def add_player(self, user, card_room):
        if not self.check_user(user, card_room):
            raise ValueError('You are registered!')
        else:
            card_room.players.add(user)
            card_room.players_count = card_room.players.count()
            card_room.save()

        if not card_room.players_count == 4:
            card_room.status = True
            card_room.seats = "Available"
            card_room.save()
        else:
            card_room.status = False
            card_room.seats = "Not Available"
            card_room.save()

    def players_waiting(self, card_rooms):
        players_count = [room.players.count() for room in card_rooms]
        return players_count
