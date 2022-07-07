"""You have two list in first you have 10 number in second you have 11 number. 10 numbers of two list are same but one is different find that number.
first  = [1,3, 5,6,7,8,12,32,7,4]
second = [1,3, 5,6,7,8,189,12,32,7,4]
Number is 189"""
x = [1,3,5,6,7,8,12,32,7,4]
y = [1,3,5,6,7,8,189,12,32,7,4]
for i in x:
    for n in y:
        if n in x:
            z = x.remove(n)
        else:
            c = n
            print("Number is > " + str(c))
