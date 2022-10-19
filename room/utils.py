from src.room_controller import Controller
from functools import cache


@cache
def get_controller():
    return Controller()
