import random


def choose_difficulty():
    print("\nChoose Difficulty:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-500)")

    choice = input("Enter choice: ")

    if choice == "1":
        return 50
    elif choice == "2":
        return 100
    elif choice == "3":
        return 500
    else:
        print("Invalid choice. Medium difficulty selected.")
        return 100


def play_game():
    maximum = choose_difficulty()
    number = random.randint(1, maximum)
    attempts = 0

    print("\nI have selected a number.")
    print("Try to guess it!")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > maximum:
                print("Please enter a number within the range.")
                continue

            attempts += 1

            if guess < number:
                print("Higher!")

            elif guess > number:
                print("Lower!")

            else:
                print("Correct!")
                print("Attempts:", attempts)
                return attempts

        except ValueError:
            print("Please enter a valid number.")


def main():
    best_attempts = None

    while True:
        attempts = play_game()

        if best_attempts is None or attempts < best_attempts:
            best_attempts = attempts
            print("New Best Score!")

        print("Best Attempts:", best_attempts)

        replay = input("\nDo you want to play again? (y/n): ")

        if replay.lower() != "y":
            print("Thanks for playing!")
            break


main()