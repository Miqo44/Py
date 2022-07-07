"""Write a Python program to count the 
 elements in a list until an element is a    
 tuple."""
num = (10,20,30,(10,20),40)
c = 0
for n in num:
    if isinstance(n, tuple):
        break
    c += 1
print(c)
