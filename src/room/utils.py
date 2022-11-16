from .controllers.room_controller import Controller
from .game_logic import GameController
from .repos.database_repo import GameData
from .validators import ValidateCards
from functools import cache


@cache
def get_controller():
    return Controller()


@cache
def game_controller():
    repository = GameData()
    validator = ValidateCards()
    return GameController(validator, repository)
