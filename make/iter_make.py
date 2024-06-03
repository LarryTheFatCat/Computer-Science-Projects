# Rock Paper Scissors Game

import random

# Ask the user if they want to play
ask = input("Would you like to play? ")

# while the user does not enter "no":
while ask != "no":
    # Not set yet
    computer_choice = None
    random_int = random.randint(1, 3)

    if random_int == 1:
        computer_choice = "rock"
    elif random_int == 2:
        computer_choice = "paper"
    else:
        computer_choice = "scissors"

    # Get user's move
    move = input("Enter your move (rock/paper/scissors): ") 
    
    # Check who wins
    if move == computer_choice:
        print("It's a tie!")
    elif move == "rock" and computer_choice == "scissors":
        print(f"You win! Computer chose {computer_choice}.")
    elif move == "paper" and computer_choice == "rock":
        print(f"You win! Computer chose {computer_choice}.")
    elif move == "scissors" and computer_choice == "paper":
        print(f"You win! Computer chose {computer_choice}.")
    else:
        print(f"You lose! Computer chose {computer_choice}.")

    # Ask the user if they want to play again
    ask = input("Would you like to play again? ")

print("Thanks for playing!")
