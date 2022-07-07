"""Take input of age of 3 people by user and determine oldest and youngest among them."""
x = int(input("1st man age>"))
y = int(input("2nd man age>"))
z = int(input("3rd man age>"))
n = max(x,y,z)
t = min(x,y,z)
print (str(n)+" is oldest!")
print (str(t)+" is youngest!")
