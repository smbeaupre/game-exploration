import numpy as np


class TicTakToe:

    def __init__(self):
        self.board = np.array([[' ', ' ', ' '],
                               [' ', ' ', ' '],
                               [' ', ' ', ' ']])

    def perform_move(self, number, val):
        # Convert number into x, y coordinates
        x, y = numpad_to_coord(number)
        self.board[y, x] = val
        return self

    def print_board(self):

        print('-------')
        for row in self.board:
            print('|'+'|'.join(row)+'|')
            print('-------')

    def get_valid_moves(self):
        coords = np.where(self.board == ' ')
        moves = []
        for i in range(len(coords[0])):
            moves.append((coords[0][i], coords[1][i]))
        for i in range(len(moves)):
            moves[i] = coord_to_numpad(moves[i][0], moves[i][1])
        return np.sort(moves)

    def is_move_valid(self, number):
        if number not in range(1, 10):
            return False
        x, y = numpad_to_coord(number)
        return self.board[y, x] == ' '

    def check_winner(self):

        for row in self.board:
            if np.all(row == row[0]) and row[0] != ' ':
                return row[0]
        for col in self.board.T:
            if np.all(col == col[0]) and col[0] != ' ':
                return col[0]
        diag_1 = self.board.diagonal()
        if np.all(diag_1 == diag_1[0]) and diag_1[0] != ' ':
            return diag_1[0]
        diag_2 = np.fliplr(self.board).diagonal()
        if np.all(diag_2 == diag_2[0]) and diag_2[0] != ' ':
            return diag_2[0]
        return ' '


def numpad_to_coord(number):

    y = int((-1 / 3) * number + 3)
    x = (number - 1) % 3
    return x, y


def coord_to_numpad(y, x):

    return 7 - (3 * y) + x
