"""Write a Python program to remove item(s) from set"""
x = {12,23,'11','hello'}
y = x.copy()
for i in x:
    y.discard(i)
    print(y)
