"""Write a python function
to multiply all numbers."""
def sum():
    x = input("Enter your numbers >")
    x = x.replace(" ",",")
    x = x.split(",")
    c = 1
    for i in x:
        if i.isdigit():
            c *= int(i)
    print(c)
sum()
