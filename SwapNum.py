#Swap Two Numbers

a = int(input('Enter A : '))
b = int(input('Enter B : '))

# First Way
'''
[a,b] = [b,a]
print(a)
print(b)
'''
# Secound Way
a = a + b  
b = a - b  
a = a - b  
print(a)
print(b)
