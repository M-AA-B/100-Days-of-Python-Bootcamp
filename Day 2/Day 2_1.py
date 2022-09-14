# Exercise 1 - Data Types


two_digit_number = int(input("Type a two digit number: "))
first_digit = two_digit_number / 10
int_first_digit = int(first_digit)
second_digit = two_digit_number % 10
sum = int_first_digit + second_digit
print(str(sum))
