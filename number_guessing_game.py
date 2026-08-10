import random

print("Welcome to the Number Guessing Game!")
print("I have chosen a number between 1 and 100.")

while True:
    secret_number = random.randint(1, 100)
    attempts = 0
    score = 100

    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1

        if guess < secret_number:
            print("Too low! Try Again!")
            score -= 10

        elif guess > secret_number:
            print("Too High! Try Again.")
            score -= 10

        else:
            print("Congratulations! You guessed the number!")
            print(f"You guessed it in {attempts} attempt(s).")
            print(f"Your score is {score}")
            break

    play_again = input("Do you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("Thanks for playing!")
        break