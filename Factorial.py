'''Write a python program which have one number.
calculate the factorial of this number.
for example 4! = 1 * 2 * 3 * 4
'''
import math
x = int(input("Enter number > "))
print (math.factorial(x))
n = 1
  
for i in range(1,x+1):
    n *=  i
      
print ("The factorial of " + str(x) + " is : ",end="")
print (n)
