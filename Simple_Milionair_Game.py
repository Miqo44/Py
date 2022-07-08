"""Create a python game Millionaire."""
x = "Vor kxzin e anvanvel i pativ haytni holandaci covagnaci? "
print(x)
y = {"a":"Madagaskar","b":"Sumatra","g":"Tasmania","d":"Kalimantan"}
z = {}
for i,n in y.items():
    z[i]=n
print("Tarberak > ",z)
z = input("Dzer patasxan@? > ")
if z == 'g':
    print("Jisht patasxann e > Tarberak 'g':Tasmania")
    print("Duq haxteciq")
else:
    print("Jisht patasxann e > Tarberak 'g' : Tasmania")
    print("duq partveciq")
