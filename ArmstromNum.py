# Armstrome Number

number = int(input("Enter a number: "))
num_digits = len(str(number))
sumnum = 0
temp_number = number
while temp_number > 0:
    digit = temp_number % 10
    sumnum += digit ** num_digits
    temp_number //= 10
if sumnum == number:
    print(f"{number} is an Armstrong number")
else:
    print(f"{number} is not an Armstrong number")
