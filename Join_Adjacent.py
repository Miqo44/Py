"""Write a Python program to join adjacent members of a given list.
Original list:
['1', '2', '3', '4', '5', '6', '7', '8']
Join adjacent members of a given list:
['12', '34', '56', '78']
"""
x = ['1', '2', '3', '4', '5', '6', '7', '8']
y = []
for i in range(0, len(x), 2):
    y.append(x[i] + x[i + 1])
print(y)
