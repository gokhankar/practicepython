# Write a program that asks the user how many Fibonnaci numbers to generate
# and then generates them. Take this opportunity to think about how you can use functions.
# Make sure to ask the user to enter the number of numbers in the sequence to generate.
# (Hint: The Fibonnaci seqence is a sequence of numbers where the next number in the
# sequence is the sum of the previous two numbers in the sequence.
# The sequence looks like this: 1, 1, 2, 3, 5, 8, 13, …)

def get_number(function_text="Gimme number"):
    return int(input(function_text))


def create_fibo():
    for i in range(3, fibo_number):
        if len(fibo_list) < fibo_number:
            new_number = fibo_list[i - 3] + fibo_list[i - 2]
            fibo_list.append(new_number)
        elif len(fibo_list) == fibo_number:
            break


fibo_number = get_number("How many Fibonnaci numbers do you want: ")
fibo_list = [1, 1]
create_fibo()
print(fibo_list)
