from objects.game import Game

game = Game()
another_game = True
while another_game:
    try:
        game.run()
    except ValueError as a:
        print(f"\nValueError for the following reason : {a}")

    except IndexError as b:
        print(f"\nIndexError for the following reason : {b}")
    finally:
        if game.play_again():
            game.__init__()     # Initialize a new game
            game.run()
        else:
            another_game = False











