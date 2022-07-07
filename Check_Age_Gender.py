"""Write a python program to check if user age in (18-20) and if gender is male."""
x = int(input("Your age > "))
y = input("Gender > ")
if x >17 and x<21 and y == "male":
    print("Yes")
else:
    print("No")
