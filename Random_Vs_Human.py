"""Write a python program which will say who win in game. 
The winner is the one which have 2 point.You should try to find pc number(0-5):
if find (your point +=1) otherwise (pc point +=1):"""
import random as r
x = int(input("nermuceq tiv"))
f = int(input("nuynic"))
t = int(input("verjinn el u gnac"))
y = r.randint(1,5)
z = 0
n = 0
if x == y:
    z+=1
else:
    n+=1
if f == y:
    z+=1
else:
    n+=1
if z == 2:
    print("you win")
elif n == 2:
    print("computer win")
elif t == y:
    z+=1
else:
    n+=1
if z == 2:
    print("you win")
else:
    print("computer win")
