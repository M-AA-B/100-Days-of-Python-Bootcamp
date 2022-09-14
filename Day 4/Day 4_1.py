# Exercise 1 - Heads or Tails

import random
test_seed = int(input("Create a seed number: "))
random.seed(test_seed)

rand_int = random.randint(0, 1)
if rand_int == 1:
    print("Heads")
else:
    print("Tails")
