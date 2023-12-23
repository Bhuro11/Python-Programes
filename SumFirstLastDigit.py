# sum of first and last digit

num = int(input("Enter a number: "))
last_digit = num % 10

while num >= 10:
    num //= 10

first_digit = num
sum_of_digits = first_digit + last_digit
print("Sum of first and last digit:", sum_of_digits)
