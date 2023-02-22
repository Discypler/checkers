import checkers

if __name__ == '__main__':
    players = [checkers.Player(1, 'white'), checkers.Player(2, 'black')]
    new_game = checkers.Game(players)
    print(new_game.id)
    print(new_game.check_possible_turns(players[0].colour))

