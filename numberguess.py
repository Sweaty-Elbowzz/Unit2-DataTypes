import random
random_number = random.randint(1, 10)
tries = 1
history = []

while True:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < random_number:
        print("Too low, try again.")
        tries += 1
        history.append(guess)
    elif guess > random_number:
        print("Too high, try again.")
        tries += 1
        history.append(guess)
    else:
        print("You guessed the correct number.:", random_number)
        print(f"It took you {tries} tries.")
        print("History: ")
        print(history)
        break

