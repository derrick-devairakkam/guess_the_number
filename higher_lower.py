import random

def guess(x):
    """ This is a guessing game in which the computer chooses a random number between 1 and 100, inclusive, and
    prompts the user to guess the number.
    """
    random_number = random.randint(1,x)
    guess = 0
    guesses = []
    while guess != random_number:
        guess = int(input(f"Guess a number between 1 and {x}: "))
        if guess not in guesses:
            guesses.append(guess)
            if guess < random_number:
                print("Sorry, guess again. Too low.")
            elif guess > random_number:
                print("Sorry, guess again. Too high.")
        else:
            print(f"You have already guessed {guess}, please guess again.")

    print(f"Congrats. You have guessed the number {random_number} correctly. Number of guesses: {len(guesses)}. ")

guess(100)
