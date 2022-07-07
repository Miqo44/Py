"""Write a python program to compute the greatest common divisor of two positive integers.
Example:
>>> input 12  8
>>> output  4"""
x = int(input("First number > "))
y = int(input("Second number > "))
c = max(x,y)
if x <= 0 or y <= 0:
    print("Enter positive integers !")
elif x == y:
    print(x)
else:
    for z in range(c,3,-2):
        if x%z == 0 and y %z == 0:
            print("Greatest common divisor is",z)
            break
    else:
        for n in range(c,2,-2):
            if x%n == 0 and y %n == 0:
                print("Greatest common divisor is",n)
                break
