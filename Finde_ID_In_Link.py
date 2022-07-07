"""Create python program where you want to find id in link if link have id print id.
Sample Input: https://www.youtube.com/watch?v=RRW2aUSw5vU
Sample Output:   RWW2aUSwvU
"""
y = input("Enter your link > ")
z = y.rfind("=")
n = int(z) +1
if z == -1:
    print("Programm not finde ID")
else:
    print(y[n:])
