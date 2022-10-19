from room.models import CardRoom


class Controller:
    # def check_users(self, user):
    #     users = CardRoom.objects.all()
    #     players = [p.player_name for p in users]
    #     print(len(players))
    #     return False if user.get_username() in players else True

    def add_player(self, user):
        p = CardRoom(status="online")
        p.save()
        p.player_name.add(user)

