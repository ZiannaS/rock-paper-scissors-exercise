# game.py

import random

print("Rock, Paper, Scissors, Shoot!")


print("Welcome 'Player One' to my Rock-Paper-Scissors game...")

# asking user for an input

userChoice = input("Please choose either 'rock', 'paper', or 'scissors': ")

# print(x)

# arguments separated by commas
#print("String one", "string 2", "string 3") 

# string concatenation:
#print("string one" + "string two")

# string interpolation
#print("You chose: {userChoice}")

print("You chose: ", userChoice, ". Let's wait for the computer!")


# simulating a computer input

options = ["rock", "paper", "scissors"]

computerChoice = random.choice(options)


print("The computer chose: ", computerChoice)

exit()

print("Oh, the computer won. It's ok.")
print("-------------------")

print("Thanks for playing. Please play again!")
