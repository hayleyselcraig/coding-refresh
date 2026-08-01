# Number Guessing Game
# The computer chooses a secret number and the user must keep guessing
# until they guess the correct number.

secret_number = 7

# Ask the user for their name and welcome them to the game
name = input("Firstly, what is your name?")
print(f"Welcome {name}! Are you ready to play the number guessing game?")
print("The computer has a secret number. Can you guess what it is?")

# Ask the user for their first guess
users_guess = int(input("What is your guess? "))

# Keep asking for guesses until the correct number is entered
while users_guess != secret_number:

    # Check if the guess is too low
    if users_guess < secret_number:
        print(f"Bad luck {name}! Too low!")

    # Check if the guess is too high
    elif users_guess > secret_number:
        print(f"Bad luck {name}! Too high!")

    # Ask the user to guess again
    users_guess = int(input("What is your guess? "))

# The loop ends once the correct number has been guessed
print("Congratulations! You guessed correctly!")