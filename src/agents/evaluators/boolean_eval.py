
def boolean_eval(game, token):

    winner = game.check_winner()
    if winner == token:
        return 10
    elif winner == ' ' or winner == 'TIE':
        return 0
    else:
        return -10
