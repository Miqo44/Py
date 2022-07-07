'''Given a number x. Check following conditions: 
 x is less or equal to -8 or x is greater than 12
 x is greater than 10 and is less or equal to 50
 x is greater than -10 and is less than 10 
 x isn’t equal to 20 or x is greater than 50
 Print the results (they should be True or False)
'''
x = int(input())
if x <=(-8) or x>12:
    print (True)
else:
    print (False)
if x >10 and x<=50:
    print(True)
else:
    print(False)
if x >(-10) and x<10:
    print (True)
else:
    print (False)
if x != 20 or x>50:
    print (True)
else:
    print(False)
