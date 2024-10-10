import random

current_min = 1
current_max = 100

def generate_random_number():
    rand_number = random.randint(current_min, current_max)
    return rand_number

def take_computer_guess(current_min:int, current_max:int):
    # Binary search step: guess the middle value between current_min and current_max
    return (current_min + current_max) // 2

def verify_computer_guess(computer_guess:int, rand_number:int):
    if computer_guess > rand_number:
        return -1  # Guess is too high
    elif computer_guess < rand_number:
        return 1   # Guess is too low
    else:
        return 0   # Correct guess

def output_commentator(computer_guess:int, rand_number:int, attempts:int):
    result = verify_computer_guess(computer_guess, rand_number)
    if result == -1:
        print(f"Lower! This is attempt number {attempts}")
    elif result == 1:
        print(f"Higher! This is attempt number {attempts}")
    else:
        print("Correct! Impressive stuff!")

def adjust_computer_bounds(current_min:int, current_max:int, computer_guess:int, rand_number:int):
    # Adjust the bounds based on whether the guess is too high or too low
    result = verify_computer_guess(computer_guess, rand_number)
    if result == -1:
        current_max = computer_guess - 1  # If guess is too high, reduce max bound
    elif result == 1:
        current_min = computer_guess + 1  # If guess is too low, increase min bound
    return current_min, current_max

if __name__ == "__main__":
    rand_number = generate_random_number()  

    attempts = 1
    computer_guess = take_computer_guess(current_min, current_max)

    print(f"The computer has guessed... {computer_guess}")

    while computer_guess != rand_number:
        output_commentator(computer_guess, rand_number, attempts)
        attempts += 1
        # Adjust the bounds based on the guess and generate a new guess
        current_min, current_max = adjust_computer_bounds(current_min, current_max, computer_guess, rand_number)
        computer_guess = take_computer_guess(current_min, current_max)  # Update guess
        print(f"The computer has guessed... {computer_guess}")

    if computer_guess == rand_number:
        print(f"Congratulations, Mr. Computer! It took you {attempts} attempts to guess correctly!")
