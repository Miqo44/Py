"""Create python program which will 
calculate the arithmetic average of 
rating students.
"""
x = {"Anna":7,"Gevor":4,"Edgar":6,"Abraham":3,"Gegham":7,"Narek":8,"Arpi":10,"Elen":6,"Arman":5,"Elya":9}
j = 0
y = len(x)
for i in x.values():
    j += i
print(j/y)
