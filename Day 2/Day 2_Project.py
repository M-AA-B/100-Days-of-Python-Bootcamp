# Tip Calculator

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
split = int(input("How many people to split the bill? "))
tip = 1 + tip/100
bill_per_person = (total_bill/split)*tip
final_amount =  round(bill_per_person,2)
print(f"Each person should pay: ${final_amount:.2f}")