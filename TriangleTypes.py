x = int(input('Enter First Sides of Triangle : '))
y = int(input('Enter Secound Sides of Triangle : '))
z = int(input('Enter Third Sides of Triangle : '))

if x == y == z:
    print("Equilateral Triangle")
elif x == y or y == z or z == x:
    print("Isosceles Triangle")
else:
    print("Scalene Triangle")
