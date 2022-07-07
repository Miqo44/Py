"""Write a python function
to sum all numbers."""
def sum():
    x = input("Enter your numbers > ")
    x = x.replace(" ",",")
    x = x.split(",")
    c = 0
    for i in x:
        if i.isdigit():
            c += int(i)
    print(c)
sum()
