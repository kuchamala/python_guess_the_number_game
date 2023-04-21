import random

# Function to generate a random number within a given range
def generate_random_number(start_range, end_range):
    return random.randint(start_range, end_range)

# Function to take user input for number of attempts allowed
def get_number_of_attempts():
    attempts = input("Enter the number of attempts allowed: ")
    return int(attempts)

# Function to take user input for guessing the number
def guess_number():
    guess = input("Guess the number: ")
    return int(guess)

# Function to compare user's guess with the generated number
def compare_numbers(random_number, guessed_number):
    if guessed_number == random_number:
        print("Congratulations! You guessed the number.")
        return True
    elif guessed_number < random_number:
        print("The number is higher. Try again.")
        return False
    else:
        print("The number is lower. Try again.")
        return False

# Main function to run the game
def run_game():
    print("Welcome to the Guess the Number game!")
    start_range = 1
    end_range = 100
    random_number = generate_random_number(start_range, end_range)
    attempts = get_number_of_attempts()

    for attempt in range(attempts):
        print(f"You have {attempts - attempt} attempts left.")
        guessed_number = guess_number()
        if compare_numbers(random_number, guessed_number):
            return
    print(f"Game over. The number was {random_number}.")

if __name__ == "__main__":
    run_game()

