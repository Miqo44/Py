"""Write a Python program to multiply all the values in a dictionary. 
For example: 
mydict = {'a':1,'b':2,'c':12} output: 24
"""
x = {'a':1,'b':2,'c':12}
y = x.values()
z = 1
for i in y:
    z *= i
print(z)
