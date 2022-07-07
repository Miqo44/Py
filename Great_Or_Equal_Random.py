"""Write a python program which will check is your number great or equal the random number of computer (10-100)if yes print True otherwise False."""
import random
x = random.randint(10,100)
y = int(input("Enter your number > "))
if y >= x :
    print(y,x)
    print(True)
else:
    print (y,x)
    print (False)
