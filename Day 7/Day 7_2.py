#Step 2

import random
word_list = ["aardvark", "baboon", "camel"]
#Testing code
size_of_list = len(word_list)
Randon_Word = random.randint(0, size_of_list - 1)
chosen_word = word_list[Randon_Word]
print(f'The solution is {chosen_word}')

#TODO-1: - Create an empty List called display.
#For each letter in the chosen_word, add a "_" to 'display'.
#So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.

#TODO-2: - Loop through each position in the chosen_word;
#If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].

#TODO-3: - Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
#Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.
Letter_Guess= input("Guess a Letter:\n").lower()
empty_list = []
for _ in chosen_word:
    empty_list.append("_")
word_len = len(empty_list)
for position in range(word_len):
    letter = chosen_word[position]
    if Letter_Guess == letter :
        empty_list[position] = Letter_Guess
print(empty_list)