#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.
# (If you don’t know what a divisor is, it is a number that divides evenly into another number.
# For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)

while True:
    divisors_list = []
    try:
        num = int(input("Type a number: "))
    except:
        print("Type only numbers please")
        continue

    for i in range(2, num+1):
        if num % i == 0:
            divisors_list.append(i)
        else:
            continue

    print(divisors_list)
    quit()
