from room.models import CardRoom


class Controller:
    def check_user(self, user, card_room):
        players = card_room.players.all()
        print(len(players))
        return user not in players

    def add_player(self, user, card_room):
        if not self.check_user(user, card_room):
            raise ValueError('fa ceva inca cazu asta')
    
        card_room.players.add(user)

    
"""

        CARD ROOM

        1                 2    
Dan Sandu Robert Constatinescu    Nicu Lenuta

"""