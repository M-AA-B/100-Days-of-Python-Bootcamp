# Exercise 5 - Love Calculator

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
both_names = name1.lower() + name2.lower()
true_count = both_names.count('t') + both_names.count('r') + both_names.count('u') + both_names.count('e')
love_count = both_names.count('l') + both_names.count('o') + both_names.count('v') + both_names.count('e')
true_love = true_count * 10 + love_count
if true_love < 10 or true_love > 90:
    print(f"Your score is {true_love}, you go together like coke and mentos.")
elif 40 < true_love < 50:
    print(f"Your score is {true_love}, you are alright together.")
else:
    print(f"Your score is {true_love}.")
