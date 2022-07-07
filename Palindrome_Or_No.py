"""Create python program where you want to check  if input word is palindrome or no .if yes print Open  otherwise Trash
Sample Input: RACECAR
Sample Output:   Open"""
x = input("nermuceq palindrome> ")
y = x[::-1]
if y == x:
    print("Open")
else:
    print("Trash")
