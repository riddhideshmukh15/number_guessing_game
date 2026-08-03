import random

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")

secret_number = random.randint(1, 100)
attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low! Try Again!")
    elif guess > secret_number:
        print("Too High! Try Again.")
    else:
        print("Congratulations! You guessed the number!")
        print(f"You guessed it in {attempts} attempt(s).")
        break