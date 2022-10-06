from whist.models import Player


class Game:
    def save_player_stats(self, player_name, hand, tricks, played_cards):
        player = Player(
            name=player_name,
            hand=hand,
            tricks=tricks,
            played_cards=played_cards,
        )
        player.save()

    def get_all_players_stats(self):
        players = Player.objects.all()

        if len(players) == 0:
            return None
        else:
            players_names = [p.name for p in players]
            hands = [p.hand for p in players]
            tricks = [p.tricks for p in players]
            played_cards = [p.played_cards for p in players]

        return [players_names, hands, tricks, played_cards]

    def remove_all(self):
        Player.objects.all().delete()

    def save_all(self, names, hands, tricks, played_cards):
        self.remove_all()
        for i in range(len(names)):
            self.save_player_stats(
                names[i],
                hands[i],
                tricks[i],
                played_cards[i]
            )
