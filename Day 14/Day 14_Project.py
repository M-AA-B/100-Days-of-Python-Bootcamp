# Higher-Lower
import os


from art import logo,vs
from game_data import data
import random

FINAL_SCORE = 0
def Print_Options():

    first_option = random.choice(data)
    second_option = random.choice(data)
    if first_option == second_option:
        second_option = random.choice(data)
    print(logo)
    f_count1 = first_option['follower_count']
    f_count2 = second_option['follower_count']
    print(f"Compare A: {first_option['name']}, {first_option['description']}, from {first_option['country']}.")
    print(vs)
    print(f"Compare B: {second_option['name']}, {second_option['description']}, from {second_option['country']}.")
    answer = input("Who has more followers? Type 'A' or 'B':").lower()
    Compare(answer,f_count1,f_count2)

def Compare(answer,f_count1,f_count2):
    global FINAL_SCORE
    right_answer = False
    if answer == "a" and f_count1 > f_count2:
        FINAL_SCORE += 1
        right_answer = True
    elif answer == "b" and f_count2 > f_count1:
        FINAL_SCORE += 1
        right_answer = True
    result(right_answer)

def result(right_answer):
    global FINAL_SCORE
    os.system('cls')
    if right_answer:
        print(f"You're right! Current score: {FINAL_SCORE}.")
        Print_Options()
    else:
        print(f"Sorry, that's wrong. Final score: {FINAL_SCORE}.")

Print_Options()
