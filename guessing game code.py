import random

def guessing_game():
    number_to_guess = random.randint(1, 100)  
    attempts = 0
    print("Welcome to the guessing game! Try to guess the number I'm thinking of (between 1 and 100).")

    while True:
        try:
            user_guess = int(input("Enter your guess: "))
            attempts += 1
            
            if user_guess < number_to_guess:
                print("Too low! Try again.")
            elif user_guess > number_to_guess:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
                break
        except ValueError:
            print("Please enter a valid number.")
            
guessing_game()