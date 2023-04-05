"""
Python Web Development Techdegree
Project 1 - Number Guessing Game
--------------------------------

For this first project we will be using Workspaces.

NOTE: If you strongly prefer to work locally on your own computer, you can totally do that by clicking: File -> Download Workspace in the file menu after you fork the snapshot of this workspace.

"""

import random

def start_game():
    """Psuedo-code Hints

    When the program starts, we want to:
    ------------------------------------
    1. Display an intro/welcome message to the player.
    2. Store a random number as the answer/solution.
    3. Continuously prompt the player for a guess.
      a. If the guess greater than the solution, display to the player "It's lower".
      b. If the guess is less than the solution, display to the player "It's higher".

    4. Once the guess is correct, stop looping, inform the user they "Got it"
         and show how many attempts it took them to get the correct number.
    5. Let the player know the game is ending, or something that indicates the game is over.

    ( You can add more features/enhancements if you'd like to. )
    """
    # write your code inside this function.
    high_score = None
    while True:
        if high_score is None:
            print("Nobody has played, yet. There is no high score set")
        else:
            print("The current high score is (least amount of guesses):", len(high_score))

        random_number = random.randint(1, 10)
        user_tries = []

        print("Welcome to the number guessing game. You need to guess a number."
              "\nThe number must be between 1 and 10."
              "\nWhen you guess the number, you win the game!!!")
        while True:
            try:
                user_guess = int(input("Input your guess: "))
            except ValueError:
                print("Incorrect value inputted! Please enter an integer.")
                continue

            if 1 <= user_guess <= 10:

                user_tries.append(user_guess)

                if user_guess == random_number:
                    print("Well done! You have guessed the number!")
                    print(f"You have the following amount of guesses:  {len(user_tries)}.")
                    break
                elif user_guess < random_number:
                    print("The number you are trying to guess is bigger. Try again!")
                else:
                    print("The number you are trying to guess is smaller. Try again!!")

                print(f"You have the following amount of guesses: {len(user_tries)}")

            else:
                print("The range is 1-10. The number you have entered is outside the range. Please, try again.")

        if high_score is None or user_tries < high_score:
            high_score = user_tries
            print("!!!HIGH SCORE!!!")

        another_round =  input("Do you want to have another round of the guessing game? (y/n): ").lower()
        if another_round != "y":
            print("Thank you for playing! Ciao!")
            break

        print("The game has ended! Thank you for playing!")
        print("------------------------------------------")
        print("------------------------------------------")
        print("------------------------------------------")

# Kick off the program by calling the start_game function.
start_game()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
