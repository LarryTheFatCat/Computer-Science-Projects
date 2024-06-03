"""
author: Tarkan Zarrouk
date: 04/03/2024
Practicing with functions
"""

import math

# TODO: Implement this function


def input_one_to_ten(prompt: str) -> int:
    """
    Allows the user to enter a number from 1 to 10.

    Use the prompt string in the input function. For example `input(prompt)`

    If the input is not numeric (again, hint) return 10.
    If the input is less than 1, return 1.
    If the input is more than 10, return 10.
    Otherwise, return the inputted number.
    """
    # Input
    num = input(prompt)
    # Processing
    if num.isnumeric() == False:  # Check whether it is like some random thing
        return 10  # Set 10,
    elif num.isnumeric():  # return true
        num = int(num)  # convert input into text
        if num < 1:
            return 1
        elif num > 10:
            return 10
        else:
            return num

# TODO: Implement this function


def factorial(n: int) -> int:
    """
    Return n factorial (the cumulative product of 1 through n, inclusive).
    n >= 0

    >>> factorial(3)
    6 # 3 x 2 x 1
    >>> factorial(5)
    120
    """
    # Output
    # Return factorial of number
    return math.factorial(n)


def main():
    # Input
    num_of_numbers = input_one_to_ten(
        "How many numbers do you want to input: ")  # Default prompt

    list_of_numbers = [] # Old list
    for _ in range(num_of_numbers): # loop over each number
        list_of_numbers.append(input_one_to_ten( 
            "Enter a number between 1 and 10: ")) # Append each number by asking via input, each input = new num in list

    # Processing (Do the list transformation)
    list_of_factorials = []  # New list to transform (before transformation, basically 0)
    for nums in list_of_numbers:  # Loop over total numbers or something
        # append to new list (your notes are awesome sir)
        list_of_factorials.append(factorial(nums)) 

    # Output
    for num in list_of_factorials:
        print(num)


if __name__ == "__main__":
    main()
