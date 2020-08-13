# The next logical step is to deal with handling user input. When a player (say player 1, who is X) wants to place
# an X on the screen, they can’t just click on a terminal. So we are going to approximate this clicking simply
# by asking the user for a coordinate of where they want to place their piece. The computer asks Player 1 (X)
# what their move is (in the format row,col), and say they type 1,3. Then the game would print out
# and ask Player 2 for their move, printing an O in that place.
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


player_1 = Player("Player 1", "X")
player_2 = Player("Player 2", "O")


def get_row():
    row = int(input("Type your move(row): "))
    return row


def get_col():
    col = int(input("Type your move(col): "))
    return col


def print_game():
    print("[" + a11 + a12 + a13 + "]")
    print("[" + a21 + a22 + a23 + "]")
    print("[" + a31 + a32 + a33 + "]")


def game_situation(row, col):
    if which_player() == player_1:
        game[row - 1][col - 1] = 1
    #       ("a"+ row + coll) = "X"
    elif which_player() == player_2:
        game[row - 1][col - 1] = 2
        print(game)
    return game


def print_situation(row, col):
    global a11, a12, a13, a21, a22, a23, a31, a32, a33
    if which_player() == player_1:
        if row == 1:
            if col == 1:
                a11 = "X"
            elif col == 2:
                a11 = "X"
            elif col == 3:
                a11 = "X"
        elif row == 2:
            if col == 1:
                a11 = "X"
            elif col == 2:
                a11 = "X"
            elif col == 3:
                a11 = "X"
        elif row == 3:
            if col == 1:
                a11 = "X"
            elif col == 2:
                a11 = "X"
            elif col == 3:
                a11 = "X"
    elif which_player() == player_2:
        if row == 1:
            if col == 1:
                a11 = "O"
            elif col == 2:
                a11 = "O"
            elif col == 3:
                a11 = "O"
        elif row == 2:
            if col == 1:
                a11 = "O"
            elif col == 2:
                a11 = "O"
            elif col == 3:
                a11 = "O"
        elif row == 3:
            if col == 1:
                a11 = "O"
            elif col == 2:
                a11 = "O"
            elif col == 3:
                a11 = "O"


def which_player():
    if count % 2 == 1:
        return player_1
    elif count % 2 == 0:
        return player_2


game = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
a11, a12, a13, a21, a22, a23, a31, a32, a33 = " ", " ", " ", " ", " ", " ", " ", " ", " ",
print("Lets play Tic Tac Toe!")
print("I will asks Player 1 (X) what his move is (in the format row and col), and say he types 1 and 3. It means: ")
print("[  X]\n[   ]\n[   ]")
print("And then if Player 2 (O) types 2 and 1. We can see: ")
print("[  X]\n[ O ]\n[   ]")
print("Lets start!")
count = 1
while True:
    print(f"{which_player().name}: It is your turn!")
    row = get_row()
    col = get_col()
    game_situation(row, col)
    print_situation(row, col)
    print(game)
    print_game()
    count += 1
