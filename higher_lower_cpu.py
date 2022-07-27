import random


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
