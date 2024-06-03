"""
author: Tarkan Zarrouk
date: 28/02/2024
Rock paper scissors game!
"""
# Input
move = input("Enter a move: ")

# Processing
while move != "rock" and move != "paper" and move != "scissors":
    move = input("Enter a move: ")

# Output
print(f"The user threw {move}")
