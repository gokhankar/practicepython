# we are trying to build up to a full tic-tac-toe board. However, this is significantly more than half an hour of
# coding, so we’re doing it in pieces. Today, we will simply focus on checking whether
# someone has WON a game of Tic Tac Toe, not worrying about how the moves were made.

# import random

"""
def random_game():
    game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for item in game:
        for elem in item:
            elem = 1
            print(game)
"""


def find_winner():
    if game[0][0] == 1 and game[0][1] == 1 and game[0][2] == 1:
        return 1
    elif game[0][0] == 2 and game[0][1] == 2 and game[0][2] == 2:
        return 2
    elif game[1][0] == 1 and game[1][1] == 1 and game[1][2] == 1:
        return 1
    elif game[1][0] == 2 and game[1][1] == 2 and game[1][2] == 2:
        return 2
    elif game[2][0] == 1 and game[2][1] == 1 and game[2][2] == 1:
        return 1
    elif game[2][0] == 2 and game[2][1] == 2 and game[2][2] == 2:
        return 2
    elif game[0][0] == 1 and game[1][0] == 1 and game[2][0] == 1:
        return 1
    elif game[0][0] == 2 and game[1][0] == 2 and game[2][0] == 2:
        return 2
    elif game[0][1] == 1 and game[1][1] == 1 and game[2][1] == 1:
        return 1
    elif game[0][1] == 2 and game[1][1] == 2 and game[2][1] == 2:
        return 2
    elif game[0][2] == 1 and game[1][2] == 1 and game[2][2] == 1:
        return 1
    elif game[0][2] == 2 and game[1][2] == 2 and game[2][2] == 2:
        return 2
    elif game[0][0] == 1 and game[1][1] == 1 and game[2][2] == 1:
        return 1
    elif game[0][0] == 2 and game[1][1] == 2 and game[2][2] == 2:
        return 2
    elif game[0][2] == 1 and game[1][1] == 1 and game[2][0] == 1:
        return 1
    elif game[0][2] == 2 and game[1][1] == 2 and game[2][0] == 2:
        return 2
    else:
        return "draw"


game = [[1, 2, 0], [2, 1, 0], [2, 1, 0]]
result = find_winner()
if result == 1 or result == 2:
    print(f"Player {find_winner()} is the winner")
else:
    print("It is a draw!")
