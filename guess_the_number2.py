import random

def main():
    print("Welcome to the Number Guessing Game!")
    print("Think of a number between 1 and 100, and I'll try to guess it.")

    low = 1
    high = 100
    attempts = 0

    while True:
        computer_guess = random.randint(low, high)
        print(f"My guess is: {computer_guess}")
        attempts += 1

        user_feedback = input("Is my guess too high (H), too low (L), or correct (C)? ").upper()

        if user_feedback == "C":
            print(f"Hooray! I guessed it in {attempts} attempts!")
            break
        elif user_feedback == "H":
            high = computer_guess - 1
        elif user_feedback == "L":
            low = computer_guess + 1
        else:
            print("Invalid input. Please enter H, L, or C.")

    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        main()
    else:
        print("Thank you for playing!")

if __name__ == "__main__":
    main()
