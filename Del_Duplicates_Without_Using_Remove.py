"""Create a python program which delete all duplicate items in list.Note: use remove()."""
x = [1,7,15,3,78,46,7,9,314,897,7,1]
x = list(dict.fromkeys(x))
print(x)
