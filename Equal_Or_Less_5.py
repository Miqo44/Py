"""Create a python program which will say 
who have 5 or little rating in your 
Students."""
x = {"Anna":7,"Gevor":4,"Edgar":6,"Abraham":3,"Gegham":7,"Narek":8,"Arpi":10,"Elen":6,"Arman":5,"Elya":9}
y = {}
n = {}
for i,l in x.items():
    if x[i] < 5:
        y[i]=l
    elif x[i] == 5:
        n[i]=l
print("Poqr e 5ic")
print(y)
print("Havasar e 5i")
print(n)
