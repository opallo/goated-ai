# Tool: Guessing Game

def guessing_game():
    
    # A simple guessing game where the user needs to guess a number between 1 and 10.

    import random

    number_to_guess = random.randint(1, 10)
    attempts = 0
    guessed = False

    print("Welcome to the Guessing Game! You need to guess a number between 1 and 10.")

    while not guessed:
        user_guess = int(input("Enter your guess: "))
        attempts += 1

        if user_guess == number_to_guess:
            print(f"Congratulations! You guessed the correct number in {attempts} attempts.")
            guessed = True
        elif user_guess < number_to_guess:
            print("Try a higher number.")
        else:
            print("Try a lower number.")

# Example Usage:
guessing_game()