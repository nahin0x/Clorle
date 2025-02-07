import random

def welcome_message():
    print("Welcome to the Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    print("You have 10 attempts to guess the correct number.")

def get_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            return guess
        except ValueError:
            print("Please enter a valid number.")

def play_game():
    welcome_message()
    
    # Randomly select a number between 1 and 100
    number_to_guess = random.randint(1, 100)
    
    attempts = 10
    
    while attempts > 0:
        print(f"\nYou have {attempts} attempts left.")
        
        guess = get_guess()
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You've guessed the number correctly!")
            break
        
        attempts -= 1
    
    if attempts == 0:
        print(f"\nSorry, you've run out of attempts. The correct number was {number_to_guess}.")

# Main function to run the game
if __name__ == "__main__":
    play_game()
