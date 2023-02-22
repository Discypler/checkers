from unittest import case

nearby_cells = ((1, 1), (1, -1), (-1, 1), (-1, -1))


class Player:
    """Class for unique player"""

    def __init__(self, _id, colour):
        self.id = _id
        self.colour = colour
        self.checkers = 12


class Game:
    """Class for unique game"""
    _id = 0

    def __init__(self, players):
        self.players = players
        self.id = self.id_counter()
        self.board = [[None for i in range(8)] for j in range(8)]
        self.queue = 'white'
        for i in range(8):
            for j in range(8):
                if i < 3 and (i + j) % 2 == 1:
                    self.board[i][j] = 'black'
                elif i > 4 and (i + j) % 2 == 1:
                    self.board[i][j] = 'white'

    @classmethod
    def id_counter(cls):
        return cls._id + 1

    @staticmethod
    def is_onboard(i, j):
        if i in range(8) and j in range(8):
            return True

    def is_enemy_colour(self, colour, i, j):
        if self.board[i][j] is not None and self.board[i][j] != colour:
            return True

    def check_possible_turns(self, colour, previous_ate='None',
                             eaten_position='None'):
        """Checking possible turns for player wit colour = colour"""
        turns_array = []
        if previous_ate is not None:
            for i in range(8):
                for j in range(8):
                    if self.board[i][j] is not None and colour in self.board[i][j]:
                        if 'king' not in self.board[i][j]:
                            for nearby_cell in nearby_cells:
                                i_check = i + nearby_cell[0]
                                j_check = j + nearby_cell[1]
                                if Game.is_onboard(i_check, j_check):
                                    cell_check = self.board[i_check][j_check]
                                    if cell_check is None:
                                        if (colour == 'white' and nearby_cell[0] == -1) \
                                                or (colour == "black" and nearby_cell[0] == 1):
                                            turns_array.append({'colour': colour, 'start_position': [i, j],
                                                                'end_position': [i_check, j_check], 'attacked': None})
                                    elif colour not in cell_check:
                                        i_attack, j_attack = i_check, j_check
                                        i_check += nearby_cell[0]
                                        j_check += nearby_cell[1]
                                        cell_check = self.board[i_check][j_check]
                                        if Game.is_onboard(i_check, j_check) and cell_check is None:
                                            turns_array.append({'colour': colour, 'start_position': [i, j],
                                                                'end_position': [i_check, j_check],
                                                                'attacked': [i_attack, j_attack]})
                        else:
                            for nearby_cell in nearby_cells:
                                block = None
                                k = 1
                                while block is not None:
                                    i_check = i + k * nearby_cell[0]
                                    j_check = j + k * nearby_cell[1]
                                    if Game.is_onboard(i_check, j_check):
                                        cell_check = self.board[i_check][j_check]
                                        if cell_check is None:
                                            turns_array.append({'colour': colour, 'start_position': [i, j],
                                                                'end_position': [i_check, j_check], 'attacked': None})
                                        else:
                                            block = [i_check, j_check]
                                    else:
                                        break
                                    k += 1
                                attacked = block
                                block = self.board[block[0]][block[1]]
                                if colour not in block:
                                    while block is not None:
                                        i_check = i + k * nearby_cell[0]
                                        j_check = j + k * nearby_cell[1]
                                        if Game.is_onboard(i_check, j_check):
                                            cell_check = self.board[i_check][j_check]
                                            if cell_check is None:
                                                turns_array.append({'colour': colour, 'start_position': [i, j],
                                                                    'end_position': [i_check, j_check],
                                                                    'attacked': attacked})
                                        else:
                                            break






        return turns_array


def start(self):
    pass


def turn(self, colour, begin, end):
    if self.board[begin] == colour:
        pass
