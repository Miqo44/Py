"""Write a Python program to check this year is leap year or no."""
x = int(input())
if x % 100 == 0 and x % 400 == 0:
    print("Yes")
else:
    print("No")
