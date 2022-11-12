from room.controllers.room_controller import Controller
from room.game_logic import GameController
from room.repos.database_repo import GameData
from room.validators import ValidateCards
from functools import cache


@cache
def get_controller():
    return Controller()


@cache
def game_controller():
    repository = GameData()
    validator = ValidateCards()
    return GameController(validator, repository)
