"""Write a Python program that have two lists and returns True if they have at least one common member."""
x = [1,7,5,6,12,4]
y = [3,9,8,14,44,1,4]
z = 0
for i in x:
    for n in y:
        if n == i:
            z +=1
if z>=1:
    print(True)
else:
    print(False)
