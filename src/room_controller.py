from room.models import CardRoom


class Controller:
    def check_user(self, user):
        users = CardRoom.objects.all()
        players = [p.players for p in users]
        print(len(players))
        return False if user.get_username() in players else True

    def add_player(self, user):
        if self.check_user(user):
            p = CardRoom()
            p.save()
            p.players.add(user)

