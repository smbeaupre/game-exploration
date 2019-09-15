import numpy as np


class Gomoku:

    def __init__(self):
        self.board = np.full((15, 15), ' ')

    def perform_move(self, coord, val):

        self.board[coord[0], coord[1]] = val
        return self

    def print_board(self):

        print('--0-1-2-3-4-5-6-7-8-9-0-1-2-3-4-')
        for i, row in enumerate(self.board):
            print(str(i)[-1]+'|'+'|'.join(row)+'|')
        print('-------------------------------')

    def get_valid_moves(self):
        coords = np.where(self.board == ' ')
        moves = []
        for i in range(len(coords[0])):
            moves.append((coords[0][i], coords[1][i]))
        return moves

    def is_move_valid(self, coord):
        return self.board[coord[0], coord[1]] == ' '

    def check_winner(self):
        if len(self.get_valid_moves()) == 0:
            return 'TIE'

        for row in self.board:
            if ('X', 'X', 'X', 'X', 'X') in zip(row, row[1:], row[2:], row[3:], row[4:]):
                return 'X'
            elif ('O', 'O', 'O', 'O', 'O') in zip(row, row[1:], row[2:], row[3:], row[4:]):
                return 'O'
        transposed = self.board.T
        for col in transposed:
            if ('X', 'X', 'X', 'X', 'X') in zip(col, col[1:], col[2:], col[3:], col[4:]):
                return 'X'
            elif ('O', 'O', 'O', 'O', 'O') in zip(col, col[1:], col[2:], col[3:], col[4:]):
                return 'X'

        for i in range(15):
            diag = self.board.diagonal(offset=i)
            if len(diag) >= 5:
                if ('X', 'X', 'X', 'X', 'X') in zip(diag, diag[1:], diag[2:], diag[3:], diag[4:]):
                    return 'X'
                if ('O', 'O', 'O', 'O', 'O') in zip(diag, diag[1:], diag[2:], diag[3:], diag[4:]):
                    return 'O'
        for i in range(15):
            diag = np.fliplr(self.board).diagonal(offset=i)
            if len(diag) >= 5:
                if ('X', 'X', 'X', 'X', 'X') in zip(diag, diag[1:], diag[2:], diag[3:], diag[4:]):
                    return 'X'
                if ('O', 'O', 'O', 'O', 'O') in zip(diag, diag[1:], diag[2:], diag[3:], diag[4:]):
                    return 'O'
        return ' '

    def get_likely_moves(self):

        pieces_o = np.where(self.board == 'O')
        tups = []
        for i in range(len(pieces_o[0])):
            tups.append((pieces_o[0][i], pieces_o[1][i]))
        pieces_x = np.where(self.board == 'X')
        for i in range(len(pieces_x[0])):
            tups.append((pieces_x[0][i], pieces_x[1][i]))

        locs = []
        recs = []
        for t in tups:

            for j in range(2):
                for k in range(2):
                    recs.append(limit_coord_to_board((t[0] + j, t[1] + k)))
                    recs.append(limit_coord_to_board((t[0] - j, t[1] + k)))
                    recs.append(limit_coord_to_board((t[0] + j, t[1] - k)))
                    recs.append(limit_coord_to_board((t[0] - j, t[1] - k)))
        recs = list(set(recs))
        for r in recs:
            if self.is_move_valid(r):
                locs.append(r)
        return list(set(locs))


def limit_coord_to_board(coord):
    y = min(max(coord[0], 0), 14)
    x = min(max(coord[1], 0), 14)

    return (y, x)