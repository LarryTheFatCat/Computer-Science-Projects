"""
author: Tarkan Zarrouk
date: 05/03/2024
FizzBuzz Game
"""

# Define Variable
number = int(input("Enter a number: "))

while number == 1:
    number = int(input("Enter a number: "))
    
for i in range(1, number + 1):
    if i % 3 == 0 and i % 5 == 0:
        print("Fizz Buzz")
    elif i % 3 != 0 and i % 5 != 0:
        print(i)
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")