"""Write a Python program that accepts a string and calculate the number of digits and letters.
string = ‘python 3.9’"""
x = "python 3.9"
y = 0
z = 0
for i in x:
    if i.isalpha():
        y += 1
    elif i.isdigit():
        z += 1
print ("tareri qanak",y," ,tveri qanak",z)
