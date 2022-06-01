# def my_sum(a, b):
#     return a + b
#
#
# def my_difference(a, b):
#     return a - b
#
#
# def my_product(a, b):
#     return a * b
#
#
# def my_quotient(a, b):
#     return a / b
#
#
# def main():
#     a = float(input("Podaj a.\n"))
#     b = float(input("Podaj b.\n"))
#
#     print(a, " + ", b, " = ", my_sum(a, b), ".", sep="")
#     print(a, " - ", b, " = ", my_difference(a, b), ".", sep="")
#     print(a, " * ", b, " = ", my_product(a, b), ".", sep="")
#
#     try:
#         print(a, " / ", b, " = ", my_quotient(a, b), ".", sep="")
#     except ZeroDivisionError:
#         print("Dzielenie przez 0.")
#
#
# main()
#
#
# # Zad 1. CodersLab - obsługa wyjątków
# def safe_get(l, index):
#     try:
#         return l[index]
#     except:
#         return None
#
#
# my_list = [1, 5, 6, "Kot"]
# print(safe_get(my_list, 3))


# Zad 2. CodersLab - obsługa wyjątków

# from random import randint
#
# guessed = False
# rnd = randint(1, 10)
#
# while not guessed:
#     try:
#         str_num = input("Enter number: ")
#         num = int(str_num)
#         if num == rnd:
#             print("Great!")
#             guessed = True
#         else:
#             print("Wrong! Try again!")
#     except ValueError as e:
#         print("It's not a number. Try again! " + e.args[0])

# # Zad 3. CodersLab - obsługa wyjątków
print("Dividing two natural numbers")
def divide(a, b):
        try:
          return a / b

        except (ValueError) as e:
            print("You must enter a number! - " + e.args[0])
            return None

        except (ZeroDivisionError) as e:
            print("You mustn't divide by 0! - " + e.args[0])
            return None

print(divide(1, 'ala'))
