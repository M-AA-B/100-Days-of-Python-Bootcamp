# Rock Paper Scissors

import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
list_ = [rock, paper, scissors]
user = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer = random.randint(0, 2)
if user == 0 and computer == 2 or user == 1 and computer == 0 or user == 2 and computer == 1:
    print(f"You chose:\n{list_[user]}\nComputer chose:\n{list_[computer]}\nYou Win!")
elif user == 1 and computer == 2 or user == 0 and computer == 1 or user == 2 and computer == 0:
    print(f"You chose:\n{list_[user]}\nComputer chose:\n{list_[computer]}\nYou Lose!")
elif user == computer:
    print(f"You chose:\n{list_[user]}\nComputer chose:\n{list_[computer]}\nIt's a Draw!")
else:
    print("Wrong Input!")
