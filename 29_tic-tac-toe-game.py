
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol


def get_row():
    while True:
        try:
            row = int(input("Type your move(ROW): "))
        except:
            print("Type a number please")
            continue
        if 0 < row < 4:
            return row
        else:
            continue


def get_col():
    while True:
        try:
            col = int(input("Type your move(COLUMN): "))
        except:
            print("Type a number please")
            continue
        if 0 < col <4:
            return col
        else:
            continue


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
#        print(game)
    return game


def print_situation(row, col):
    global a11, a12, a13, a21, a22, a23, a31, a32, a33
    if which_player() == player_1:
        if row == 1:
            if col == 1:
                a11 = "X"
            elif col == 2:
                a12 = "X"
            elif col == 3:
                a13 = "X"
        elif row == 2:
            if col == 1:
                a21 = "X"
            elif col == 2:
                a22 = "X"
            elif col == 3:
                a23 = "X"
        elif row == 3:
            if col == 1:
                a31 = "X"
            elif col == 2:
                a32 = "X"
            elif col == 3:
                a33 = "X"
    elif which_player() == player_2:
        if row == 1:
            if col == 1:
                a11 = "O"
            elif col == 2:
                a12 = "O"
            elif col == 3:
                a13 = "O"
        elif row == 2:
            if col == 1:
                a21 = "O"
            elif col == 2:
                a22 = "O"
            elif col == 3:
                a23 = "O"
        elif row == 3:
            if col == 1:
                a31 = "O"
            elif col == 2:
                a32 = "O"
            elif col == 3:
                a33 = "O"


def which_player():
    if count % 2 == 1:
        return player_1
    elif count % 2 == 0:
        return player_2


def control_game():
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


player_1 = Player("Player 1", "X")
player_2 = Player("Player 2", "O")
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
#    print(game)
    print_game()
    if control_game() == 1:
        print("Player 1 won! Congratulations!")
        quit()
    elif control_game() == 2:
        print("Player 2 won! Congratulations!")
        quit()
    element_list = []
    for item in game:
        for elem in item:
            element_list.append(elem)
    if 0 not in element_list:
        print("Game Over! It is a tie!")
        quit()
    count += 1
