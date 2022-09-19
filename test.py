from whist.game_logic.domain.entity import Player
from whist.game_logic.repository.game_repository import GameData
from whist.game_logic.domain.validate import ValidateCards
from whist.game_logic.services.controller import Controller
import pytest

@pytest.fixture
def test_file_path(tmp_path):
    d = tmp_path / "sub"
    d.mkdir()
    temp_path = d / 'test_file.txt'
    
    temp_path.write_text('')
    return temp_path

@pytest.fixture
def test_positions_file_path(tmp_path):
    d = tmp_path / "sub2"
    d.mkdir()
    temp_path = d / 'test_positions.txt'
    
    temp_path.write_text('')
    return temp_path



def test_add_trick_to_player_adds_one_point_to_the_winner_when_called(test_file_path, test_positions_file_path):
    card_validator = ValidateCards()
    repository = GameData(test_file_path, test_positions_file_path)
    controller = Controller(card_validator, repository)

    game = controller.load_game()

    player_names = game['players_names']
    winner = player_names[0]
    players = [Player(p) for p in player_names]

    controller.add_trick_to_player(winner, players)
