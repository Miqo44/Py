"""Write a Python program to count the number of even and odd numbers from a series of numbers(1-100)."""
i = 1
x = 0
y = 0
z = int(input("nermuceq tiv > "))
while i <=z:
    if i%2 == 1:
        x+=1
    elif i%2 == 0:
        y+=1
    i+=1
print ("kent tveri qanak > "+str(x)+", zuyg tveri qanak > " +str(y))
