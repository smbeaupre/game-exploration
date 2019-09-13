import random


class RandomPlayer:

    def __init__(self, token):
        self.token = token

    def get_move(self, game):

        return random.choice(game.get_valid_moves())
