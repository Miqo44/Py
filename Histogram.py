''' Write a python program to create a histogram in one print from given number. You know that your number have three-digit. Example:
>>> input 254
>>> output          **
                    *****
                    ****
'''
x = int(input("Enter your number > "))
if x < 100 :
    print("Enter number with 3 digits")
else:
    z = x // 100
    c = (x-z*100)//10
    b = x % 10
    y = '*'
    print (z * y)
    print (c * y)
    print (b * y)
