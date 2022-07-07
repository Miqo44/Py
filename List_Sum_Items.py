"""Write a Python program to
  sum all the items in a list."""
x = [1, 3, 4, 5, 1, 2, 3, 1]
y = sum(x)
print(y)
x = [1, 3, 4, 5, 1, 2, 3, 1]
y = 0
for i in x:
    y += i
print(y)
