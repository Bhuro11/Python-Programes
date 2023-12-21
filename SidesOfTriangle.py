#WAP 3 numbers check number is side of triangle
n3 = int(input("Enter Number 1 : "))
n4 = int(input("Enter Number 2 : "))
n5 = int(input("Enter Number 3 : "))

if n3+n4>=n5 and n4+n5>=n3 and n5+n3>=n4:
    print("Sides of Triangle")
else:
    print("Not Sides of Triangle")
