import random
import string

words = ['smoothie', 'water', 'waiter', 'dog', 'traffic']


class PartialHangman:

    def __init__(self):
        self.word = random.choice(words)
        self.letters_guessed = []
        self.most_recent_player = ' '

    def perform_move(self, letter, player_token):
        # Convert number into x, y coordinates
        self.letters_guessed.append(letter)
        self.most_recent_player = player_token
        return self

    def print_board(self):

        output = []
        for l in self.word:
            if l in self.letters_guessed:
                output.append(l)
        print('Letters in word:', output)
        print('Letters guessed:', self.letters_guessed)

    def get_valid_moves(self):

        letters = string.ascii_lowercase
        output = []
        for l in letters:
            if l not in self.letters_guessed:
                output.append(l)
        return output

    def is_move_valid(self, letter):

        return (letter in string.ascii_lowercase) and (len(letter) == 1) and (letter not in self.letters_guessed)

    def check_winner(self):

        for l in self.word:
            if l not in self.letters_guessed:
                return ' '

        return self.most_recent_player
