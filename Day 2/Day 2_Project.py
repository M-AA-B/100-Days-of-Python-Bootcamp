"""
Tip Calculator
If the bill was $150.00, split between 5 people, with 12% tip.

Each person should pay (150.00 / 5) * 1.12 = 33.6

Format the result to 2 decimal places = 33.60

Thus everyone's share of the total bill is $30.00 plus a $3.60 tip.

"""

print("Welcome to the tip calculator.")
bill = float(input("What was the total bill?"))
percentage = int(input("What percentage tip would you like to give? 10, 12, or 15?"))
num_people = int(input("How many people to split the bill?"))

tip = bill * percentage / 100
individual_tip = (bill + tip) / num_people
print(f"Each person should pay: ${round(individual_tip, 2)}")
