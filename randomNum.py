"""
    create random number between 1-9 inclusive.
    ask the user to guess the number, tell them
    whether they guessed, too high, too low, or
    they were exactly right.
"""

import random

random = random.randint(1,9)
guess = int(input("Guess a number 1-9>>>>"))

while guess!=random:
    if guess > random:
        print("too high")
        guess = int(input("Guess a number 1-9>>>>"))
    elif guess < random:
        print("too low")
        guess = int(input("Guess a number 1-9>>>>"))
    else:
        guess = int(input("Guess a number 1-9>>>>"))
print("You got it! You win!")            
        
            
