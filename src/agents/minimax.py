import random
import time
from copy import deepcopy
from src.agents.evaluators import boolean_eval


class MinimaxPlayer:

    def __init__(self, token, max_depth=8, search_time=15, move_selection='Valid'):
        self.token = token
        self.max_depth = max_depth
        self.move_selection = move_selection
        self.number_searches = 0
        self.search_time = search_time
        if self.token == 'O':
            self.min_token = 'X'
        else:
            self.min_token = 'O'

    def get_move(self, game):

        max_time = time.time() + self.search_time

        best_move = ""

        for d in range(self.max_depth+1):
            print('Searching depth:', d)
            score, move = self._minimax(current_game=game, current_depth=0, max_depth=d, is_max_turn=True, max_time=max_time)
            print(self.number_searches, move, score)
            self.number_searches = 0

            if move != 'TIMEOUT':
                best_move = move

        if best_move == "":
            if len(game.get_likely_moves()) == 0:
                return random.choice(game.get_valid_moves())
            else:
                return random.choice(game.get_likely_moves())
        return best_move

    def _minimax(self, current_game, current_depth, max_depth, is_max_turn, max_time, evaluator=boolean_eval, alpha=float('-inf'), beta=float('inf')):

        if time.time() >= max_time:
            return float('-inf'), 'TIMEOUT'

        if is_max_turn:
            current_token = self.token
        else:
            current_token = self.min_token

        if current_game.check_winner() != ' ' or current_depth == max_depth or time.time() >= max_time:
            return evaluator(current_game, self.token), ""

        if self.move_selection == 'Likely':
            possible_moves = current_game.get_likely_moves()
        else:
            possible_moves = current_game.get_valid_moves()
        random.shuffle(possible_moves)
        best_move = ""
        best_value = float('-inf') if is_max_turn else float('inf')

        for move in possible_moves:
            self.number_searches += 1

            new_game = deepcopy(current_game).perform_move(move, current_token)

            eval_child, action_child = self._minimax(current_game=new_game, current_depth=current_depth + 1, max_depth=max_depth, max_time=max_time, is_max_turn=not is_max_turn, alpha=alpha, beta=beta)

            if is_max_turn and best_value < eval_child:
                best_value = eval_child
                best_move = move
                alpha = max(alpha, best_value)
                if beta <= alpha:
                    break

            elif (not is_max_turn) and best_value > eval_child:
                best_value = eval_child
                best_move = move
                beta = min(beta, best_value)
                if beta <= alpha:
                    break

        return best_value, best_move