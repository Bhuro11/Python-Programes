# Murphy No

n = int(input("Enter Number : "))
m = n
c = 0
while n>0 :
        c+=1
        n=n//10
        s=m*n
        p=10**c
        x=s%p
        if m==x :
            print(m, "Is Murphy")
        else :
            print(m, "Is Not Murphy")
            
        
