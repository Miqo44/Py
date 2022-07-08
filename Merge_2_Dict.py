"""Write a Python program to merge two Python dictionaries.
dict1 = {'a': 50, 'b': 700}
dict2 = {'c': 400, 'd': 600}
output: {'a': 50, 'b': 700, 'c': 400, 'd': 600}"""
x = {'a': 50, 'b': 700}
y = {'c': 400, 'd': 600}
x.update(y)
print(x)
