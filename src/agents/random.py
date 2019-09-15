import random


class RandomPlayer:

    def __init__(self, token, move_selection='Likely'):
        self.token = token

    def get_move(self, game):

        if self.move_selection == 'Likely':
            possible_moves = game.get_likely_moves()
        else:
            possible_moves = game.get_valid_moves()

        return random.choice(possible_moves)
