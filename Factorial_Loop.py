"""Write a loop to find the factorial of any number. You have one input."""
x = int(input())
y = 1
for i in range(1,x+1):
    y *=i
print(y)
""" OR > import math
x = int(input())
print (math.factorial(x))"""
