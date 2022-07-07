"""Create a python program which will say which number used more.
my_list = [1, 3, 4, 5, 1, 2, 3, 1]
output:  number 1 - 3 times"""
x = [1,3,4,5,1,2,3,1,3,3,3]
n = 0
for i in x:
    y = x.count(i)
    if y > n:
        z = i
        n = y
    else:
        print( " number " + str(z) + " - " + str(n) + " times" )
        break
