import random
import numpy as np
import ast

from src.players import HumanPlayer, RandomPlayer


def numpad_to_coord(number):

    y = int((-1 / 3) * number + 3)
    x = (number - 1) % 3
    return x, y


class Game:

    def __init__(self):
        self.board = np.array([[' ', ' ', ' '],
                               [' ', ' ', ' '],
                               [' ', ' ', ' ']])

    def update_board(self, number, val):
        # Convert number into x, y coordinates
        x, y = numpad_to_coord(number)
        self.board[y, x] = val
        return self

    def print_board(self):

        print('-------')
        for row in self.board:
            print('|'+'|'.join(row)+'|')
            print('-------')

    def is_move_valid(self, number):
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

    def play_game(self, player1, player2):
        game_over = False
        player_order = [player1, player2]
        random.shuffle(player_order)

        current_player = player_order[0]
        waiting_player = player_order[1]
        while not game_over:
            self.print_board()
            valid_move = False
            while not valid_move:
                desired_move = current_player.get_move()
                valid_move = self.is_move_valid(desired_move)
                if not valid_move:
                    print('Invalid move, try again')
            self.update_board(desired_move, current_player.token)
            winner = self.check_winner()
            if winner == ' ':
                current_player, waiting_player = waiting_player, current_player
                print()
            else:
                break
        print('WINNER: ' + winner)
        self.print_board()


g = Game()
g.play_game(player1=HumanPlayer('X'), player2=RandomPlayer('O'))

