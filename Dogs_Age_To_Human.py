"""Write a Python program to calculate a dog's age in human years.
Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years."""
x = float(input())
y = 0
if x <=2:
    y = 10.5*x
elif x > 2:
    y = 2 * 10.5 + ((x-2)*4)
    print (y)
