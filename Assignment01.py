print('PRIME NUMBERS BETWEEN 1 TO 200')
for num in range(1, 200 + 1):
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num, end=' ')
