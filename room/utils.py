from src.room_controller import Controller
from src.game_logic import GameController
from src.database_repo import GameData
from src.validate import ValidateCards
from functools import cache


@cache
def get_controller():
    return Controller()


@cache
def game_controller():
    repository = GameData()
    validator = ValidateCards()
    return GameController(validator, repository)
