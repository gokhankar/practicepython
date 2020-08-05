
def say_me_odd_or_even():
    while True:
        try:
            num = input("Give me  a number: ")
            if num == "q":
                break
            num2 = int(num)
            if num2 % 2 == 0:
                print(f"{num2} is even")
            else:
                print(f"{num2} is odd")

        except:
            print("Give me a number or 'q' to quit!")


say_me_odd_or_even()