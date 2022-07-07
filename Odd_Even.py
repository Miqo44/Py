"""Write a python program to check how much odd and even number have your number.
For example 103  have 52 odd and 51 even
"""
c = int(input("Enter number to check odd and even >"))
a = 0
b = 0
if c %2 ==1:
    a= c//2+1
    b= c//2
    print(str(a) + " Odd " + str(b) + " Even")
else:
    a = c//2
    b = a
    print(str(a) + " Odd " + str(b) + " Even")
