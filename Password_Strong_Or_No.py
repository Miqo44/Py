"""Create python program which will check if your password is strong or no.
if Len your password is great than 8,
and if your password have 2 numbers,
and 2 of the following special characters ('!', '@', '#', '$', '%', '&', '*')
Sample Input:    Python@$World11
Sample Output:   Strong"""
x = input("gaxtnabar > ")
z = 0
n = 0
c = ("!",'@',"#",'$','%','&','*')
for i in x:
    if i.isdigit():
        z += 1
    elif i in c:
        n += 1
if len(x) > 8 and z > 1 and n > 1:
    print("Your password is :Strong")
else :
    print("Your password is :Weak")
