"""Write a python program to compute the smallest number that is divisible by both integer a and b. 
Example:
>>> input 14 8
>>> output 2"""
x = int(input("First number > "))
y = int(input("Second number > "))
if x < 2 or y < 1:
    print("One of numbers less then 2")
elif x % 2 == 0 and y % 2 == 0:
    print("Smallest divisible number is >",2)
else:
    for n in range(3,9,2):
        if x%n == 0 and y %n == 0:
            print("Smallest divisible number is >",n)
            break
