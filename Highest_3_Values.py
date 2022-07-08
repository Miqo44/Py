"""Create a Python program to find the highest 3 values in a dictionary.
{'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
output: {'F': 69, 'A': 67, 'D': 56}
"""
x = {'D': 56, 'E': 12, 'F': 69, 'C': 45, 'B': 23, 'A': 67}
y = {}
n = sorted(x, key=x.get,reverse = True)
j = 0
for i in n:
    y[i] = x[i]
    j +=1
    if j ==3:
        break
print(y)
