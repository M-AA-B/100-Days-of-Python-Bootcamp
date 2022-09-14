#Step 3




import random
word_list = ["aardvark", "baboon", "camel"]
end_of_game = False
#Testing code
size_of_list = len(word_list)
Randon_Word = random.randint(0, size_of_list - 1)
chosen_word = word_list[Randon_Word]
print(f'The solution is {chosen_word}')

#TODO-1: - Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.
empty_list = []
for _ in chosen_word:
    empty_list.append("_")
word_len = len(empty_list)

while not end_of_game:
    Letter_Guess= input("Guess a Letter:\n").lower()
    for position in range(word_len):
        letter = chosen_word[position]
        if Letter_Guess == letter :
            empty_list[position] = Letter_Guess
    print(*empty_list)
    if "_" not in empty_list:
        print("You win!")
        end_of_game = True