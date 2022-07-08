"""Create a python program which will say 
if your dictionary have this name 
print name and rating.
"""
x = {"Anna":7,"Gevor":4,"Edgar":6,"Abraham":3,"Gegham":7,"Narek":8,"Arpi":10,"Elen":6,"Arman":5,"Elya":9}
y = input("Anun > ")
n = {}
for i,l in x.items():
    if y in x:
        n[y]=l
        print("Anun : Rateing")
        print(n)
        break
    else:
        print("Aydpisi anun chka bararanum")
        break
