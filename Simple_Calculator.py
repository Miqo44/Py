"""Write a python function to create a simple Calculator."""
x = input("What u want to do? '+', '-', '/', '*', '^' > ")
a = int(input("Enter your first number > "))
b = int(input("Enter your second number > "))
def calc(a,b):
    if x == '+':
        return a+b
    elif x == '-':
        return a-b
    elif x == '/':
        return a/b
    elif x == '*':
        return a*b
    elif x == '^':
        return a**b
print(calc(a,b))
