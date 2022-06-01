import random


def random_average(n):
    sum_of_numbers = 0
    your_list = []
    for i in range(1, n + 1):
        your_list.append(random.randint(1, 100))
        sum_of_numbers = sum_of_numbers + your_list[i - 1]
    return print(f'The arithmetic average of numbers on {your_list} is {sum_of_numbers / n}.')

try:
    user_number = int(input("Enter number of numbers: "))
    random_average(user_number)

except ValueError as e:
    print("Only natural numbers! - " + e.args[0])
