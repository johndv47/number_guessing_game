'''
script: pinto_number_guess.py
action: a. generate a random integer
        b. request user input to guess the randomly generated integer
        c. keep count of user guesses
        d. give hints i.e. higher or lower
        e. customized message based on number of guesses
author: John Pinto
date: 2/2/2026
'''
import random

# Initializes game loop
play_again = "y"


while play_again == "y":
    # Generates random integer in between 1 and 1000
    roll = random.randrange(1, 1001)
    #print(roll) -- remove # to solve the secret

    # Initialize guess counter
    guesses = 0

    # Request users guess & adds +1 to users guesses
    guess = int(input("Guess my number between 1 and 1000 with the fewest guesses: "))
    guesses += 1

    # Checks user input & compares to randomly generated integer (roll)
    while guess != roll:
        # Display hints to the user
        if guess > roll:
            print("Too high! Try again.")
        else: 
            print("Too low! Try again.")

        # Request users next guess
        guess = int(input("Guess again: "))
        guesses += 1

    # Displays customized message based on number of guesses
    if guesses > 10:
        print(f"\nCongratulations. You guessed the number!")
        print(f"You should be able to do better!")
    else:
        print(f"\nCongratulations. You guessed the number!")
        print(f"Either you know the secret or you got lucky!")

    # Play again?
    play_again = str(input("Play again? (y)es or (n)o: ")).lower()