# working with variables and functions

import random
# Variables
name = "John"
age = 25
name1, HEIGHT, my_name, _name, name1 = "John", 25, "John", "John", "John"

# player_choice = "rock"
# computer_choice = "paper"
x = 1 + 1 # example of statement


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

# working with nested functions
def main_function():
    def nested_function():
        print("Hello from nested function")
    nested_function()

# example of closure. Definition: A closure is a function that remembers the values from the enclosing lexical scope even
#     when the program flow is no longer in that scope.
def outer_function():
    x = 2
    def inner_function():
        print(x)
    return inner_function

# Call the function
print(get_choice("rock"))
print(who_wins("rock", "paper"))
print(who_wins("rock", "scissors"))
print(who_wins("paper", "rock"))
print(who_wins("paper", "scissors"))
print(who_wins("scissors", "rock"))
main_function()
closure = outer_function()
closure()