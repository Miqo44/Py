"""Chinga Chung"""
import random
i = 1
x = int(input("1@ qarn e,2@ tuxt,3@ mkrat>"))
while i < 2 :
    y = random.randint(1,3)
    if x == y:
        print ("Voch voqi")
    elif x == 1 and y == 3:
        print ("Duq haxteciq")
    elif x > y:
        print ("Duq haxteciq")
    elif y == 1 and x == 3:
        print ("Duq partveciq")
    elif y > x:
        print ("Duq partveciq")
    i += 1
print(str(y)+" hamakargchi @ntrutyun")
