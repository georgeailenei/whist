
from operator import pos


class GameData:
    def __init__(self, file_name, file_positions):
        self.file_name = file_name
        self.file_positions = file_positions
        self.players_names = []
        self.hands = []
        self.removed_players_cards = []
        self.tricks = []
        self.board = None
        self.score_one = 0
        self.score_two = 0
        self.trump_card = None
        self.played_card = None
        self.player_pos = 0
    
    def save_player_pos(self, position):
        with open(self.file_positions, 'a') as file:
            file.write(str(position) + '\n')

    def get_player_pos(self):
        with open(self.file_positions, 'r') as file:
            lines = file.readlines()
            if len(lines) == 0:
                return self.player_pos
            else:
                return lines[-1]

    def load_file_data(self):
        with open(self.file_name, 'r') as file:
            lines = file.readlines()
            return lines

    def save_played_card(self, card):
        self.remove_played_card()
        with open(self.file_name, "a") as file:
            file.write("played_card" + " : " + str(card) + "\n")

    def get_played_card(self):
        self.get_all()
        return self.played_card

    def remove_played_card(self):
        with open(self.file_name, 'r') as file:
            lines = file.readlines()

        if lines[-1].split(" : ")[0] == 'played_card':
            del lines[-1]

            with open(self.file_name, 'w') as file:
                for line in lines:
                    file.write(line)

    def save_all(self, players, hands, tricks, board, score_one, score_two, trump_card, removed_cards):
        self.remove_all()
        with open(self.file_name, "a") as file:
            all_players = [player for player in players]
            all_hands = [" ".join(hand) for hand in hands]
            all_removed_cards = [" ".join(cards) for cards in removed_cards]
            all_tricks = [str(trick) for trick in tricks]
            the_board = [str(card) for card in board]

            for i in range(len(all_players)):
                file.write(all_players[i] + " : " + all_hands[i] + " : " + all_tricks[i] + " : " + all_removed_cards[i] + "\n")

            file.write("board" + " : " + ",".join(the_board).replace(',', ' ') + "\n")
            file.write("scores" +  " : " + str(score_one) + " : " + str(score_two) + "\n")
            file.write("trump" +  " : " + str(trump_card) + "\n")

    def remove_all(self):
        file = open(self.file_name, "w")
        file.close()

    def get_all(self):
        with open(self.file_name, "r") as file:
            lines = file.readlines()
            name, hand, trick, removed_cards = 0, 1, 2, 3
            score_one, score_two = 1, 2
            board, trump_card = 1, 1
            card = 1

            if len(lines) == 0:
                return 'empty_file'
            elif len(lines) > 0:
                for line in lines:
                    info = line.split(" : ")
                    info[-1] = info[-1][:-1]
                    
                    if info[name] == 'board':
                        self.board = info[board].split()
                    elif info[name] == 'trump':
                        self.trump_card = info[trump_card]
                    elif info[name] == 'scores':
                        self.score_one = int(info[score_one])
                        self.score_two = int(info[score_two])
                    elif info[name] == 'played_card':
                        self.played_card = info[card]
                    else:
                        self.players_names.append(info[name])
                        self.tricks.append(int(info[trick]))
                        self.hands.append(info[hand].split())   
                        self.removed_players_cards.append(info[removed_cards].split())   
