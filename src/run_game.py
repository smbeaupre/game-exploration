import random
from src.games import TicTakToe, PartialHangman, Gomoku
from src.agents import HumanPlayer, RandomPlayer, MinimaxPlayer


def play_game(game, player1, player2):
    game_over = False
    player_order = [player1, player2]
    random.shuffle(player_order)

    current_player = player_order[0]
    waiting_player = player_order[1]
    while not game_over:
        game.print_board()
        valid_move = False
        while not valid_move:
            desired_move = current_player.get_move(game=game)
            valid_move = game.is_move_valid(desired_move)
            if not valid_move:
                print('Invalid move, try again')
        game.perform_move(desired_move, current_player.token)
        winner = game.check_winner()
        if winner == ' ':
            current_player, waiting_player = waiting_player, current_player
            print()
        else:
            break
    print('WINNER: ' + winner)
    game.print_board()

game = Gomoku()
play_game(game=game, player1=HumanPlayer('X'), player2=MinimaxPlayer('O', max_depth=6, move_selection='Likely'))



