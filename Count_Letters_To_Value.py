"""Create a dictionary from a string.
Get the count of the letters from the string.
word = ‘exercises’
output: {“e”:3,”x”:1,”r”:1,”c”:1,”i”:1,”s”:2}
"""
x = input("Enter some word > ")
y = {}
for i in x:
    n = x.count(i)
    y.setdefault(i)
    y[i] = n
print(y)
