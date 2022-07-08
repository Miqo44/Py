"""Write a Python program to remove an item from a set if it is present in the set."""
x = {12,23,'11','hello'}
y = input("Your item is? > ")
if y in x:
    print("Your item is on list and it will be removed!")
    x.discard(y)
elif int(y) in x:
    print("Your item is on list and it will be removed!")
    x.discard(int(y))
else:
    print("Your item is not on list!")
print(x)
