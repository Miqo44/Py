"""Your group have 5 people and each of them can take one name and when take this name is delete from this list.
And he can not take his name:"""
x = input("Anun > ")
y = ["Anna","Artak","Emil","Elen","Abgar"]
if x in y:
    print(str(x) + " Is on list and that name will be removed")
    y.remove(x)
    print(y)
else:
    print(x + " Is not in list")
