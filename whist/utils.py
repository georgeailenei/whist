from whist.game_logic.services.controller import Controller
from whist.game_logic.domain.validate import ValidateCards
from whist.game_logic.repository.game_repository import GameData
from functools import cache


@cache
def get_controller():
    card_validator = ValidateCards()
    repository = GameData('game_data.txt', 'player_position.txt')
    return Controller(card_validator, repository)
