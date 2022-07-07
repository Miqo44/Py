"""Write a python program which will check is your number equal the random number of computer (1-10)if yes print True otherwise False."""
import random
x = random.randint(0,10)
y = int(input("Enter your number > "))
if x == y :
    print (True)
    print(str(y) + " < is your number " + str(x) + " Is computers number.")
else:
    print (False)
    print(str(y) + " < is your number " + str(x) + " Is computers number.")
