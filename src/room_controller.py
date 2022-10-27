

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
            card_room.seats = "Available"
            card_room.save()
        else:
            card_room.seats = "Not Available"
            card_room.save()

    def check_players_num(self, card_rooms):
        return card_rooms.players.count()

    def get_players_names(self, card_room):
        players = [player for player in card_room.players.all()]
        return players

    def remove_player(self, user, card_room):
        card_room.players.remove(user)
        card_room.players_count = card_room.players.count()
        card_room.save()

    def get_room_status(self, card_room):
        return card_room.status

    def change_status_to_false(self, card_room):
        card_room.status = False
        card_room.save()

    def change_status_to_true(self, card_room):
        card_room.status = True
        card_room.save()
