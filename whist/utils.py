from whist.game_logic.services.controller import Controller
from whist.game_logic.domain.validate import ValidateCards
from src.database_repository import GameData
from functools import cache


@cache
def get_controller():
    card_validator = ValidateCards()
    repository = GameData()
    return Controller(card_validator, repository)
