# Exercise 2 - Banker Roulette

import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
rand_int = random.randint(0, len(names)-1)
rand_choice = names[rand_int]
print(f"{rand_choice} is going to buy the meal today!")
