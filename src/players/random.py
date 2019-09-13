import random


class RandomPlayer:

    def __init__(self, token):
        self.token = token

    def get_move(self):
        return random.randint(1, 9)
