

class GameController:
    def __init__(self, card_validator, repository):
        self.card_validator = card_validator
        self.repository = repository

    def load_game(self, room):
        content = self.repository.load_game_stats(room)
        return {
            'board': content['board'],
            'trump_card': content['trump_card'],
            'score1': content['team_one_score'],
            'score2': content['team_two_score'],
            'player_pos': content['player_position'],
            'played_card': content['played_card'],
            'players_names': content['players_names'],
            'players_cards': content['players_cards'],
            'players_tricks': content['players_tricks'],
            'removed_players_cards': content['removed_players_cards'],
        }

    def check_card(self, card):
        return self.card_validator.check_card(card)

    def save_card(self, card):
        self.repository.save_played_card(card)
