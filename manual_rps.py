# Rock, Paper, Scissors game code

import random as rnd

# list of options
options = ["rock", "paper", "scissors"]

# Get the choice from the computer
def get_computer_choice():
    
    return rnd.choice(options)

# Get the choice from the user
def get_user_choice():
    
    return input("Please enter your choice: ")

# Use computer and user choices to establish the winner
def get_winner(computer_choice, user_choice):

    print(f"You: {user_choice}\nMe: {computer_choice}")

    if (computer_choice == "rock" and user_choice == "paper") or (computer_choice == "paper" and user_choice == "scissors") or (computer_choice == "scissors" and user_choice == "rock"):
        return "You won!"

    elif (user_choice == "rock" and computer_choice == "paper") or (user_choice == "paper" and computer_choice == "scissors") or (user_choice == "scissors" and computer_choice == "rock"):
        return "You lost!"
    else:
        return "It is a tie"

# Play the game by calling the above two functions
def play():

    print(get_winner(get_computer_choice(), get_user_choice()))

# Play the game
play()