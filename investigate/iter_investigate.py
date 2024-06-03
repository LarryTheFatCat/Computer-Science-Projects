"""
author: Tarkan Zarrouk
date: 02/27/2023
Iteration Investigation
"""

separator = "-" * 10

# Prints this sentence 5 times
# TODO: Print this sentence 7 times
for i in range(7):
    print("I love corn.")

print(separator)

# Prints numbers from 0 to 9
# TODO: Print numbers from 1 to 20
for i in range(0, 21):
    print(i)

print(separator)

# Prints all the even numbers from 0 to 30
# TODO: Print all the odd numbers from 1 to 100
for i in range(1, 101, 2):
    print(i)

print(separator)

# Asks the user to input a word until it is exactly 6 letters long
# TODO: Ask the user to input a word until it is longer than 10 letters
# Use the prompt: 'Please enter a word longer than 10 letters: '

# Input
word = input("Please enter a word longer than 10 letters: ")
while len(word) < 10:
    # Processing
    word = input("Please enter a word longer than 10 letters: ")
# TODO: Change the print below to: print(f'Your long word is {word}')
# Output
print(f'Your long word is {word}')

print(separator)

# Asks the user to input a word until it starts with a capital
# TODO: Ask the user to input a word until the whole word is uppercase [Google]
# Use the prompt: 'Please enter an uppercase word: '
word = input("Please enter an uppercase word: ")
while not word.isupper():
    word = input("Please enter an uppercase word: ")
# TODO: Change the print below to: print(f'Your uppercase word is: {word}')
print(f'Your uppercase word is: {word}')

print(separator)

# TODO: Ask the user for input until their input `is_numeric`` (hint hint).
# after the while loop, convert the user's input to an integer!
number = input("Please enter a number: ")
# While loop goes here
while not number.isnumeric():
    number = input("Please enter a number: ")

number = int(number)
print(type(number))
