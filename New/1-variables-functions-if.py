# working with variables and functions

# Variables
import random


# player_choice = "rock"
# computer_choice = "paper"

# Functions
def get_choice(player_choice):
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    choices = {"player": player_choice, "computer": computer_choice}
    # choice = input("Please choose rock, paper, or scissors: ")
    return choices

def who_wins(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif player_choice == "rock":
        if computer_choice == "paper":
            return "The computer won!"
        else:
            return "You won!"
    elif player_choice == "paper":
        if computer_choice == "scissors":
            return "The computer won!"
        else:
            return "You won!"
    elif player_choice == "scissors":
        if computer_choice == "rock":
            return "The computer won!"
        else:
            return "You won!"
    else:
        return "Please choose rock, paper, or scissors."


# Call the function
print(get_choice("rock"))
print(who_wins("rock", "paper"))
print(who_wins("rock", "scissors"))
print(who_wins("paper", "rock"))
print(who_wins("paper", "scissors"))
print(who_wins("scissors", "rock"))
