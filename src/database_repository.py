from whist.models import Player


class Game:
    def save_player_stats(self, player_name, hand, tricks, played_cards, position):
        player = Player(
            name=player_name,
            hand=hand,
            tricks=tricks,
            played_cards=played_cards,
            player_position=position
        )
        player.save()

    def get_all_players_stats(self):
        players_stats = Player.objects.all()

        players_names = [name for name in Player.name]
        hands = [hand for hand in Player.hand]
        tricks = [trick for trick in Player.tricks]
        played_cards = [cards for cards in Player.played_cards]
        positions = [pos for pos in Player.player_position]

        return players_names, hands, tricks, played_cards, positions
