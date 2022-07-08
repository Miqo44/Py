"""Write a Python program to find maximum and the minimum value in a set."""
x = {12,27,34,'13',65,54,'103','112',2,564}
y = x.copy()
c = x.copy()
for i in x:
    for n in x:
        if int(n) > int(i):
            y.discard(i)
        elif int(n) < int(i):
            c.discard(i)
print("Max value of this set is ",y)
print("Min value of this set is ",c)
