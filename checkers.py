from unittest import case

import numpy


class Player:
    """Class for unique player"""

    def __init__(self, id, colour):
        self.id = id
        self.colour = colour
        self.checkers = 12


nearby_cells  = ((1, 1), (1, -1), (-1, 1), (-1, -1))

def is_onboard(i, j):
    if i in range(8) and j in range(8):
        return True

class Game:
    """Class for unique game"""

    def __init__(self, players, id):
        self.players = players
        self.id = id
        self.board = matrix = numpy.empty(shape=(8, 8), dtype='object')
        self.queue = 'white'
        for i in range(8):
            for j in range(8):
                if i < 3 and (i + j) % 2 == 1:
                    self.board[i][j] = 'black'
                elif i > 4 and (i + j) % 2 == 1:
                    self.board[i][j] = 'white'

    def is_enemy_colour(self, i, j):
        if self.board[i][j]

    def check_possible_turns(self, colour, previous_ate='None',
                             eaten_position='None'):
        """Checking possible turns for player wit colour = colour"""
        turns_array = []
        if not previous_ate:
            for i in range(8):
                for j in range(8):
                    if colour in self.board[i][j]:
                        if 'king' not in self.board[i][j]:
                            for nearby_cell in nearby_cells:
                                i_check = i + nearby_cell[0]
                                j_check = j + nearby_cell[1]
                                if is_onboard(i_check, j_check):
                                    cell_check = self.board[i_check][j_check]
                                    if cell_check is None:
                                        turns_array.append({'colour': colour, 'start_position': [i, j],
                                                            'end_position': [i_check, j_check], 'attacked': None})
                                    elif cell_check != colour:
                                        i_check += nearby_cell[0]
                                        j_check += nearby_cell[1]
                                        if is_onboard(i_check, j_check) and self.board[i_check][j_check] != N





def start(self):
    pass


def turn(self, colour, begin, end):
    if self.board[begin] == colour:
        pass