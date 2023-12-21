# Print Elecricity Bill
units = int(input('Enter Units'))

if (units <= 100):
      
        bill = units * 10; 
     
    elif (units <= 200):
     
        bill = ((100 * 10) +
                (units - 100) * 15); 
     
    elif (units <= 300):
      
        bill = ((100 * 10) +
                (100 * 15) +
                (units - 200) * 20); 
     
    elif (units > 300):
     
        bill = ((100 * 10) +
                (100 * 15) +
                (100 * 20) +
                (units - 300) * 25); 

print('Your Bill',bill)
