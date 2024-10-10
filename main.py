import random

def generate_random_number():
    rand_number = random.randint(1, 100)
    return rand_number

def take_user_input():
    user_guess = int(input("Please input your guess, player.\n\n"))
    return user_guess


def verify_user_input(rand_number:int, user_guess:int, attempts:int):
    if user_guess > rand_number:
        return "Lower! Hah, this is attempt number ", attempts
    elif user_guess < rand_number:
        return "Higher! Hah, this is attempt number ", attempts
    else:
        return "Correct!"

if __name__ == "__main__":
    rand_number = generate_random_number()
    attempts = 1

    user_guess = take_user_input()

    while(user_guess != rand_number):
        print(verify_user_input(rand_number, user_guess, attempts))
        if(user_guess != rand_number):
            user_guess = take_user_input()
            attempts += 1
        else:
            break
    
    print("Congratulations, it only took you ", attempts, " attempts!")
