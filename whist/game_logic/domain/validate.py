from .entity import Deck


class ValidateCards:
    def check_card(self, card: str):
        deck = Deck().cards
        return True if card in deck else False

    def check_players_cards(self, card: str, player_cards: list):
        return True if card in player_cards else False

    def check_right_suit(self, card: str, player_cards: list, suit: str, trump_card: str):
        s = -1
        player_suits = [card[s] for card in player_cards]

        if suit is None:
            return True
        elif card[s] == suit:
            return True
        elif card[s] == trump_card and suit not in player_suits:
            return True
        elif card[s] != suit and card[s] != trump_card and suit not in player_suits and trump_card not in player_suits:
            return True
        else:
            return False
