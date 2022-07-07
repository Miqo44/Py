"""Write a python program which have 2 input (angle of triangle) and calculate the size of the third angle.
30, 60, ---> 90
"""
a = int(input("First angle >"))
b = int(input("Second angle >"))
c = 180 - (a + b)
print(c)
