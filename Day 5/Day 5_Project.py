# Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))
nr_symbols = int(input("How many symbols would you like?\n"))
total_number = nr_letters + nr_numbers + nr_symbols
random_password = ""
list_ = []

for i in range(0, nr_letters):
    rand_letter = random.randint(0, 25)
    list_.append(letters[rand_letter])

for j in range(0, nr_numbers):
    rand_number = random.randint(0, 9)
    list_.append(numbers[rand_number])

for k in range(0, nr_symbols):
    rand_symbol = random.randint(0, 8)
    list_.append(symbols[rand_symbol])

random.shuffle(list_)
for m in list_:
    random_password += m

print(f"Your Password is: {random_password}")
