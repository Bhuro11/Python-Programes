# Swap Three Numbera
a = int(input('Enter A : '))
b = int(input('Enter B : '))
c = int(input('Enter C : '))

a = a + b + c
b = a - (b + c)
c = a - (b + c)
a = a - (b + c)
print(a)
print(b)
print(c)


