# Enter Your Annual Income that print Income Tax as per your income
ai = int(input('Enter Your Anual Income : '))

if ai <= 500000:
    tax = "No Tax"
elif ai <= 1000000:
    tax = (ai - 500000) * 0.1
elif ai <= 2000000:
    tax = (ai - 1000000) * 0.2 + 50000
else : 
    tax = (ai - 2000000) * 0.3 + 250000

    print('Tax Is = ', tax)
