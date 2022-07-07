"""Write a Python program to select the odd items of a list. And delete even items."""
x = [1,3,5,7,9,11,13,15,17,19,2,4,6,8,10]
z = " "
n = " "
for i in x:
    if i%2==0:
        n += str(i)+z
    else:
        x.remove(i)
print(n.split())
