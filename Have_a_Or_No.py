'''Write a python program to check have your name ‘a’ or no.You have 2 input.'''
a = input()
b = input()
if a.count(a)>=1 or b.count(a)>=1:
    print(True)
else:
    print(False)
