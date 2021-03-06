# In the game of Hangman, a clue word is given by the program that the player has to guess, letter by letter.
# The player guesses one letter at a time until the entire word has been guessed. (In the actual game, the player can
# only guess 6 letters incorrectly before losing). Let’s say the word the player has to guess is “EVAPORATE”.
# For this exercise, write the logic that asks a player to guess a letter and displays letters in the clue word
# that were guessed correctly. For now, let the player guess an infinite number of times until they get the entire word.
# As a bonus, keep track of the letters the player guessed and display a different message if the player tries to guess
# that letter again. Remember to stop the game when all the letters have been guessed correctly!
# Don’t worry about choosing a word randomly or keeping track of the number of guesses the player has remaining.


import random


def pick_a_word():
    with open('sowpods.txt', 'r') as f:
        my_list = f.readlines()
    return random.choice(my_list).strip()


def printing():
    p_word = ""
    for elem in print_screen:
        p_word = p_word + elem + " "
    return p_word


def get_letter():
    letters = "QWERTYUOPASDFGHJKLIZXCVBNM"
    print(printing())
    while len(letter_list) < len(list_word):
        letter = input("Type a letter please: ").upper()
        if letter in letters and len(letter) == 1:
            if letter not in all_letters:
                all_letters.append(letter)
                if letter in list_word:
                    if letter not in str(letter_list):
                        letter_list.append(letter)
#                        print(letter_list)
                        return letter
                else:
                    print(f"{letter} is not a letter of my word")
                    break
            else:
                print(f"You typed {letter} previously")
                continue
        else:
            print("Letters are here: QWERTYUOPASDFGHJKLIZXCVBNM")
            continue


def letter_search():
    count = 0
    for item in list_word:
        if item == lt:
            print_screen[count] = lt
            count += 1
        else:
            count += 1
            continue


def same_letters():
    lw = set(list_word)
    re_count = 0
    for item in list_word:
        if item in lw:
            lw.remove(item)
        else:
            re_count += 1
    return re_count


print("I have a word, try to find!")
word = pick_a_word()
# print(word)
letter_list = []
all_letters = []
list_word = list(word)
print_screen = []
for i in list_word:
    if i in letter_list:
        print_screen.append(i)
    else:
        print_screen.append("_")
# print(list_word)
last_count = 0
r = same_letters()
while (len(list_word) - r) > len(letter_list):
    last_count += 1
    lt = get_letter()
    letter_search()
if (len(list_word) - r) == len(letter_list):
    print(printing())
    print(f"Congratulations! Bingo at {last_count}. try")
