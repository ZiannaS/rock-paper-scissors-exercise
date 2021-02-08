# game.py

import random
from dotenv import dotenv_values

# import choice functionality from random module
# from random import choice 

#Get player name from environment variables
config = dotenv_values(".env")

# Changing Player one to name
print("Welcome " + config['PLAYER_NAME']+" to my Rock-Paper-Scissors game!")

# asking user for an input
# validating input

userChoice = input("Please choose either 'rock', 'paper', or 'scissors': ")
userChoice.lower() 
options = ["rock", "paper", "scissors"]

if userChoice not in options:
    print("Oops, please choose a valid option and try again!")
    exit()

# print(x)

# arguments separated by commas
#print("String one", "string 2", "string 3") 

# string concatenation:
#print("string one" + "string two")

# string interpolation
#print("You chose: {userChoice}")

print("You chose: ", userChoice, ". Let's wait for the computer!")

# validate the user selection
# stop the program (not try to determine the winner)
# ... if the user choice is invalid





# simulating a computer input


computerChoice = random.choice(options)


print("The computer chose: ", computerChoice)

# validate the user selection
# stop the program (not try to determine the winner)
# ... if the user choice is invalid

userChoice.lower()

if userChoice not in options:
    print("Oops, please choose a valid option and try again!")
    exit()
    


# determining who won


if computerChoice == userChoice:
    print("It's a draw!")
elif userChoice == "paper" and computerChoice == "rock":
    print("You win! Congrats")
elif userChoice == "paper" and computerChoice == "scissors":
    print("Oh! The computer won, that's ok!")
elif userChoice == "rock" and computerChoice == "paper":
    print("Oh! The computer won, that's ok!")
elif userChoice == "rock" and computerChoice == "scissors":
    print("You win! Congrats")
elif userChoice == "scissors" and computerChoice == "paper":
    print("You win! Congrats")
elif userChoice == "scissors" and computerChoice == "rock":
    print("Oh! The computer won, that's ok!")


print("Thanks for playing. Please play again!")
