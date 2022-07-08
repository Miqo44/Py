"""Create a python program which says 
good and bad students names and ratings.
"""
x = {"Anna":7,"Gevor":4,"Edgar":6,"Abraham":3,"Gegham":7,"Narek":8,"Arpi":10,"Elen":6,"Arman":5,"Elya":9}
y = {}
n = {}
for i,l in x.items():
    if x[i] < 5:
        y[i]=l
    else:
        n[i]=l
print("Bad students")
print(y)
print("Good students")
print(n)
