'''Write a Python program to check if pc number is great than 10. random(1,20)
when True break.'''
import random
i = 1
x = 10
while i < 10:
    y = random.randint(0,20)
    print (y ,x)
    
    if y < 10:
        break
    i += 1
