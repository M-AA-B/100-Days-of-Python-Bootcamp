# Step 5

import random
from hangman_art import stages
from hangman_art import logo
from hangman_words import word_list

print(logo)
# Testing code
size_of_list = len(word_list)
Randon_Word = random.randint(0, size_of_list - 1)
chosen_word = word_list[Randon_Word]

# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
# Delete this line: word_list = ["ardvark", "baboon", "camel"]
lives = 6
end_of_game = False
# TODO-2: - Import the stages from hangman_art.py and make this error go away.
# Create blanks
empty_list = []
for _ in chosen_word:
    empty_list.append("_")
word_len = len(empty_list)

print(*empty_list)
# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.

while not end_of_game:
    Letter_Guess = input("Guess a Letter:\n").lower()


    for position in range(word_len):
        letter = chosen_word[position]

        if Letter_Guess == letter:
            empty_list[position] = Letter_Guess
        if Letter_Guess not in chosen_word or Letter_Guess == " ":
            print(stages[lives])
            lives -= 1
            break
# TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
        if Letter_Guess in empty_list and position == word_len - 1:
            print(f'{Letter_Guess} is in the word')
            break
# TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        if Letter_Guess not in empty_list and position == word_len - 1:
            print(f'{Letter_Guess} is not in the word')
    print(*empty_list)

# Then reduce 'lives' by 1.
# If lives goes down to 0 then the game should stop and it should print "You lose."
    if lives == 0:
        print(stages[lives])
        print("You lose!")
        end_of_game = True
        print(f'The solution is {chosen_word}')

if "_" not in empty_list:
    print("You win!")
    end_of_game = True