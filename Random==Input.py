'''Write a python program which have a string of number (5 number 1-10).
Your comp will try to find one of them.
Use random module if find True otherwise False.'''
import random
x = ['1','2','3','4','5','6','7','8','9','10']
random.shuffle(x)
y = int(input("nermuceq tiv > "))
for i in x:
    if int(i) == y:
        print (True)
        break
    else:
        print (False)
        break
print(x[0] + " < Hamakargchi tiv.")
print(str(y) + " < Nermucac tiv.")
