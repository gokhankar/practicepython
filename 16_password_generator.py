# Write a password generator in Python.
# Be creative with how you generate passwords - strong passwords have a mix of lowercase letters,
# uppercase letters, numbers, and symbols. The passwords should be random,
# generating a new password every time the user asks for a new password.
# Include your run-time code in a main method.
# Ask the user how strong they want their password to be.
# For weak passwords, pick a word or two from a list.
import random


def weak_password():
    print(random.choice(word_list) + random.choice(word_list))


def strong_password():
    print(random.choice(word_list) + random.choice(symbols) + random.choice(uppercase) + random.choice(numbers) + random.choice(word_list))


def extra_strong_password():
    print(random.choice(word_list) + random.choice(symbols) + random.choice(uppercase) + random.choice(numbers) + random.choice(word_list) + random.choice(word_list) + random.choice(symbols) + random.choice(uppercase) + random.choice(numbers) + random.choice(word_list))


lowercase = ["q", "w", "e", "r", "t", "y", "u", "o", "p", "a", "s", "d", "f", "g", "h", "j", "k", "l", "i", "z", "x", "c", "v", "b", "n", "m"]
uppercase = ["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G", "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M"]
numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]
symbols = ["!", "+", "%", "&", "/", "=", "?", "*", "-", "_", "@", "$", "<", ">"]
word_list = ["banana", "apple", "honey", "bear", "love", "hate", "milk", "cow"]
print("I will generate a password for you")
print("If you want a weak password, type 'w'")
print("If you want a strong password, type 's'")
print("If you want a extra-strong password, type 'e'")

while True:
    choice = input("Type your choice: ")
    if choice == "w":
        weak_password()
    elif choice == "s":
        strong_password()
    elif choice == "e":
        extra_strong_password()
    else:
        print("w/s/e ?")
