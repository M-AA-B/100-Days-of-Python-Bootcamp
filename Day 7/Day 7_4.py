# Step 4

import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
end_of_game = False
# Testing code
size_of_list = len(word_list)
Randon_Word = random.randint(0, size_of_list - 1)
chosen_word = word_list[Randon_Word]
print(f'The solution is {chosen_word}')
# TODO-1: - Create a variable called 'lives' to keep track of the number of lives left.
lives = 6


# Create blanks
empty_list = []
for _ in chosen_word:
    empty_list.append("_")
word_len = len(empty_list)


# TODO-2: - If guess is not a letter in the chosen_word,
# Then reduce 'lives' by 1.
# If lives goes down to 0 then the game should stop and it should print "You lose."
while not end_of_game:
    Letter_Guess = input("Guess a Letter:\n").lower()
    for position in range(word_len):
        letter = chosen_word[position]
        if Letter_Guess == letter:
            empty_list[position] = Letter_Guess
# TODO-3: - print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
        if Letter_Guess not in chosen_word:
            print(stages[lives])
            lives -= 1
            break

    print(*empty_list)
    if lives == 0:
        print(stages[lives])
        print("You lose!")
        end_of_game = True

    if "_" not in empty_list:
        print("You win!")
        end_of_game = True
