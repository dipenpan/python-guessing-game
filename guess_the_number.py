import random

def play_game():
    myNum = random.randint(1, 100)  # Random number generated outside the loop
    attempt = 0
    score = 0

    while True:
        attempt += 1
        
        try:
            # Asking number from the users
            user_guess = int(input("Guess the number between 1 and 100: "))
        except ValueError:
            print("Invalid input! Please enter a valid integer.\n")
            continue
        
        # Checking the conditions
        if user_guess <= 0 or user_guess > 100:
            print("Please enter a valid integer between 1 and 100.\n")
            continue
        elif user_guess < myNum:
            print("Your guessed number is too low. Try again!")
        elif user_guess > myNum:
            print("Your guessed number is too high. Try again!")
        else:
            print("Congratulations! YOU WON!")
            score = max(0, 10 - attempt)  # Score calculation
            print(f"Your final score is: {score}")
            break

    # Asking user if they want to play again or not
    ask = input("Do you want to play again? YES/NO: ").strip().upper()
    if ask == "YES":
        play_game()  # Recursively call the function to play again
    else:
        print("Thank you for playing!")

# Start the game
play_game()

        
        