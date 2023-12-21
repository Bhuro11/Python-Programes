# WAP to Enter 3 Marks to print, pass,fail,atkt
m1 = int(input("Enter Marks 1 : "))
m2 = int(input("Enter Marks 2 : "))
m3 = int(input("Enter Marks 2 : "))
c = 0

if m1>=40:
    c = c+1

if m2>=40:
    c = c+1

if m3>=40:
    c = c+1

if c == 3:
    print("You Are Pass");
    
if c == 2:
    print("ATKT");
    
if c <= 1:
    print("Sorry, Try To Next Time");
