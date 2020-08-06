# Ask the user for a number and determine whether the number is prime or not.
# (For those who have forgotten, a prime number is a number that has no divisors.)
# Take this opportunity to practice using functions.......

def number_input():
    return int(input("Please type a number: "))


def prime_control():
    if my_number < 2:
        print(f"{my_number} is not a prime number")
        quit()
    elif my_number == 2 or my_number == 3:
        print(f"{my_number} is a prime number")
        quit()
    else:
        for i in range(2, my_number):
            if my_number % i == 0:
                print(f"{my_number} is not a prime number")
                quit()
        print(f"{my_number} is a prime number!")
        quit()


while True:
    try:
        my_number = number_input()
    except:
        print("Please give me only numbers")
        continue

    prime_control()
