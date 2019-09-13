import ast


class HumanPlayer:

    def __init__(self, token):
        self.token = token

    def get_move(self, game):
        return ast.literal_eval(input('Select move position (1-9): '))
