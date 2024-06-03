"""
author: Tarkan Zarrouk
date: 04/02/2024
A skip counter that is written in python
"""

# Input
num_1 = int(input("Please enter a number: "))
num_2 = int(input("Please enter a second number: "))
skip_counter = int(input("What would you like to go up by: "))

while num_1 > 100 and num_1 < 100 and num_2 < num_1:
    num_1 = int(input("Please enter a number: "))
    num_2 = int(input("Please enter a second number: "))
    skip_counter = int(input("What would you like to go up by: "))
    
if skip_counter == "ones":
    for i in range(num_1, num_2):
        print(i)
elif skip_counter == "twos":
    for i in range(num_1, num_2):
        print(i % 2 + 2)
    elif skip_counter == "fives":