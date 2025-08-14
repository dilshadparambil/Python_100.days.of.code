import random
import art

EASY_LEVEL=5
HARD_LEVEL=10

def check(user_guess, actual_number,total_turns):
    if user_guess>actual_number:
        print("Too high.")
        return total_turns-1
    elif user_guess<actual_number :
        print("Too low.")
        return total_turns - 1
    else:
        print(f"You got it! The answer was {actual_number}.")

def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print(art.logo)
    print("Welcome to the Number Guessing Game!\n"
          "I'm thinking of a number between 1 and 100.")

    number=5#random.randint(1,100)

    turns=set_difficulty()
    print(f"You have {turns} attempts remaining to guess the number.")

    guess=0
    while guess!=number:
        guess = int(input("Make a guess: "))
        turns=check(guess,number,turns)
        if turns==0:
            print("You've run out of guesses. Restart the game to run again.")
            return
        elif guess!=number:
            print("Guess again.")



game()