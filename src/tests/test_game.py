import pytest
from room.utils import game_controller, get_controller
from room.models import CardRoom
from userauth.models import User
from room.entities import Deck

controller = get_controller()
game = game_controller()


def create_player(username):
    user = User.objects.create(username=username)
    return user


@pytest.fixture
def cards():
    return [
        "3d",
        "Kh",
        "8c",
        "4h",
        "6c",
        "2h",
        "10h",
        "3s",
        "9s",
        "Jc",
        "Js",
        "Ah",
        "5s",

        "2c",
        "10s",
        "6d",
        "4c",
        "Qh",
        "2d",
        "10c",
        "7h",
        "7d",
        "Kc",
        "Ad",
        "7c",
        "4d",

        "8d",
        "Ks",
        "3c",
        "Qs",
        "5d",
        "4s",
        "Qd",
        "6h",
        "7s",
        "9h",
        "2s",
        "10d",
        "5c",


        "8s",
        "Jh",
        "Qc",
        "9c",
        "Kd",
        "As",
        "6s",
        "Jd",
        "8h",
        "9d",
        "5h",
        "Ac",
        "3h",
    ]

@pytest.fixture
def ready_card_room(cards):
    card_room = CardRoom.objects.create()
    player1 = create_player("player1")
    player2 = create_player("player2")
    player3 = create_player("player3")
    player4 = create_player("player4")
    controller.add_player(player1, card_room)
    controller.add_player(player2, card_room)
    controller.add_player(player3, card_room)
    controller.add_player(player4, card_room)
    game.setup_room(card_room, cards)
    return card_room


def test_run_removes_player_card_from_hand_when_valid_card_is_played(
    db, ready_card_room
):
    player1 = ready_card_room.players.first()
    game.run(ready_card_room, "3d", "", "")
    player1.refresh_from_db()
    assert player1.hand.split() == [
        "Kh",
        "8c",
        "4h",
        "6c",
        "2h",
        "10h",
        "3s",
        "9s",
        "Jc",
        "Js",
        "Ah",
        "5s",
    ]


def test_run_increases_player_position_when_valid_card_is_played(db, ready_card_room):
    game.run(ready_card_room, "3d", "", "")
    ready_card_room.refresh_from_db()
    assert ready_card_room.stats.player_position == 1


def test_run_sets_player_position_to_winner(db, ready_card_room):
    game.run(ready_card_room, "3d", "", "")
    game.run(ready_card_room, "6d", "", "")
    game.run(ready_card_room, "10d", "", "")
    game.run(ready_card_room, "9d", "", "")
    ready_card_room.refresh_from_db()
    assert ready_card_room.stats.player_position == 2


def test_run_add_points_to_winner(db, ready_card_room):
    player3 = ready_card_room.players.all()[2]
    game.run(ready_card_room, "3d", "", "")
    game.run(ready_card_room, "6d", "", "")
    game.run(ready_card_room, "10d", "", "")
    game.run(ready_card_room, "9d", "", "")
    player3.refresh_from_db()
    assert player3.tricks == 1
