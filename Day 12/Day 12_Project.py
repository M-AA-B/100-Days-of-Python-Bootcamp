# Guessing Game

from art import logo
import random

end_of_game = False
def Guessing_function(rand_num, att):
    while att > 0:
        print(f"You have {att} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        if guess == rand_num:
            print(f"You got it! The answer was {rand_num}")
            break
        elif guess < rand_num:
            att -= 1
            print("Too low.\nGuess again.")
            
        elif guess > rand_num:
            att -= 1
            print("Too high.\nGuess again.")
while not end_of_game:
    print(logo)
    print("Welcome tothe Number Guessing Game!")
    print("I am thinking of a number between 1 and 100.")
    random_number = random.randint(1,100)
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == "easy":
        attempts = 10
    elif difficulty == "hard":
        attempts = 5
    Guessing_function(rand_num=random_number, att = attempts)
    play_again = input("Do you want to play again ? Type 'yes' or 'no' ").lower()
    if play_again != "yes":
        end_of_game = True