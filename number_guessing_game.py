import random


print("   NUMBER GUESSING GAME")
high_score = 0

while True:

    print("\nChoose Difficulty Level:")
    print("1. Easy (10 attempts)")
    print("2. Medium (7 attempts)")
    print("3. Hard (5 attempts)")

    level = input("Enter your choice (1/2/3): ")

    if level == "1":
        max_attempts = 10
    elif level == "2":
        max_attempts = 7
    elif level == "3":
        max_attempts = 5
    else:
        print("Invalid choice! Defaulting to Medium.")
        max_attempts = 7

    secret_number = random.randint(1, 100)
    attempts = 0
    score = 100

    print("\nI have chosen a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it!")

    while attempts < max_attempts:

        try:
            guess = int(input("\nEnter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too Low! Try Again!")

        elif guess > secret_number:
            print("Too High! Try Again!")

        else:
            print("\nCongratulations! You guessed the number!")
            print("Number was:", secret_number)
            print("Attempts used:", attempts)

            score = max(0, 100 - (attempts - 1) * 10)

            print("Your Score:", score)

            if score > high_score:
                high_score = score
                print("New High Score!")

            break

        print("Attempts left:", max_attempts - attempts)

        if attempts == 3:
            if secret_number % 2 == 0:
                print("Hint: The secret number is EVEN.")
            else:
                print("Hint: The secret number is ODD.")

    else:
        print("\nGame Over! You have used all your attempts.")
        print("The correct number was:", secret_number)

    print("\nYour Highest Score:", high_score)

    play_again = input("\nDo you want to play again? (yes/no): ").lower()

    if play_again != "yes":
        print("\nThanks for playing!")
        print("Your Final High Score:", high_score)
        break