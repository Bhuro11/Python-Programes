# No is Palindrome or not

num = int(input("Enter a number: "))
num_str = str(num)
reverse_str = num_str[::-1]
if num_str == reverse_str:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")
