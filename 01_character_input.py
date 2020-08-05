#Create a program that asks the user to enter their name and their age.
#Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Say me your name: ")
while True:
    try:
        age = int(input("Say me your age: "))
    except:
        print("Give me only numbers please")
        continue
    year = 2020 + (100 - age)
    print(f"Hey {name}! You will be 100 years old, in year {year}")
    quit()
