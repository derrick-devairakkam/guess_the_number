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



def computer_guess(X):
    """ This guessing game is the inverse of above. The user chooses the number to guess and the computer
    takes turns guessing.
    """
    low = 1
    high = X
    feedback = ""
    c_guesses = []
    while feedback != "c":
        if low!= high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)? ").lower()
        c_guesses.append(guess)
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    print(f"I gotcha, your number is {guess}! It took me {len(c_guesses)} tries")

computer_guess(100)
