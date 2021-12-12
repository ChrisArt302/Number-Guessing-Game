# A number guessing game

import random


# generates a random number between 1 and 10
number = random.randint(1, 10)
guess = 0
tries = 0

used_guesses = []

while guess != number:
    try:
        guess = (input("Guess a number between 1 and 10: "))
        guess = int(guess) # Converted input (i.e. string) to integer:

        # if guess is valid then add to the list of used guesses
        if guess in range(1, 11):
            used_guesses.append(guess)

            # if correct
            if guess == number:
                tries += 1
                print('Correct, you got it right!')
                if tries == 1:
                    print('It took you', tries, "try.")
                elif tries > 1:
                    print('It took you', tries, "tries.")

            # if duplicate guess
            elif used_guesses.count(guess) > 1:
                print("You've already used that number.\n")
                tries += 1
                continue

            # if wrong
            elif guess != number:
                tries += 1
                print('Wrong, please guess again.\n')

        if guess not in range(1, 11): # last number not included
            print("Number outside of range.\n")

    except ValueError: # no tries are counted if this is raised
        print("Please enter a number\n")









