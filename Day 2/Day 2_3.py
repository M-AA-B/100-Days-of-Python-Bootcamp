# Exercise 3 - Life in Weeks

age = int(input("What is your current age?"))

r_age = 90 - age
r_months = r_age * 12
r_weeks = r_age * 52
r_days = r_age * 365
print(f"You have {r_days} days, {r_weeks} weeks, and {r_months} months left.")
