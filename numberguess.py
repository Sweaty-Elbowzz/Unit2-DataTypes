import random
random_number = random.randint(1, 200)
tries = 1

while True:
    user_guess = int(input("Guess a number between 1 and 50: "))
    if user_guess < random_number:
        print("Too low, try again.")
        tries += 1
    elif user_guess > random_number:
        print("Too high, try again.")
        tries += 1
    else:
        print("You guessed the correct number.:", random_number)
        print(f"It took you {tries} tries.")
        break