"""Write a Python program to get the Fibonacci series between 0 to 40: 
Fib_num = 0,1,1,2,3,5,8 ….."""
x = int(input("How many terms? > "))
z, n = 0, 1
count = 0
if x <= 0:
   print("Please enter a positive integer")
elif x == 1:
   print("Fibonacci sequence upto ",x," :")
   print(z)
else:
   print("Fibonacci sequence:")
   while count < x:
       print(z)
       y = z + n
       z = n
       n = y
       count += 1
