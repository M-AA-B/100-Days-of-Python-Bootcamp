# Exercise 4 - Pizza Order Practice

print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
bill = 0
if size == "L":
    bill += 25
elif size == "M":
    bill += 20
else:
    bill += 15
if add_pepperoni == "Y":
    if size == "L" or size == "M":
        bill += 3
    elif size == "S":
        bill += 2
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")
