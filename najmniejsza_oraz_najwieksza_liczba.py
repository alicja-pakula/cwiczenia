import random

my_list = []

for i in range(1, 100):
    my_list.append(random.randint(1, 200))
print("My list: ", my_list)

my_min = my_list[0]
my_max = my_list[1]

for j in my_list:
    if j < my_min:
        my_min = j
    if j > my_max:
        my_max = j

print("The smallest number in my list is", my_min, "and the biggest number is", my_max)
