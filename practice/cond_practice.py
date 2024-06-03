"""
author: Tarkan Zarrouk
date: 21/02/2024
Two sort and three sort python conditionals practice
"""


# Input
num_1 = int(input("Enter one number: "))
num_2 = int(input("Enter a second number: "))
num_3 = int(input("Enter a third number: "))

# Processing / output
if num_1 < num_2 < num_3:
    print(f"{num_1} {num_2} {num_3}")
elif num_2 < num_1 < num_3:
    print(f"{num_2} {num_1} {num_3}")
elif num_3 < num_1 < num_2:
    print(f"{num_3} {num_1} {num_2}")
elif num_1 < num_3 < num_2:
    print(f"{num_1} {num_3} {num_2}")
elif num_2 < num_3 < num_1:
    print(f"{num_2} {num_3} {num_1}")
elif num_3 < num_2 < num_1:
    print(f"{num_3} {num_2} {num_1}")
else:
    print("The numbers are equal.")
