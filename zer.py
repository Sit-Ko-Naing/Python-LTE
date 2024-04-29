# for loop  | while loop | do while loop

import random

player1 = 0
player2 = 0

is_game_on = True

while is_game_on:
    player1 = player1 + random.randint(1,100)
    player2 = player2 + random.randint(1,100)

    if player1 > 100:
        print(f"Player1 win the game with {player1} marks")
        is_game_on = False
    elif player2 > 100:
        print(f"Player2 win the game with {player2} marks")
        is_game_on = False

   