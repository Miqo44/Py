#yete 2 hat nuynic ka updatei vaxt poxuma 1ini tex@ 2rordna dnum
"""Create a new dictionary:
For example…
s = 'a,2,b,5,c,8,a,4,e,11'
{“a”:6,”b”:5,”c”:8,”e”:11}"""
x = 'a,2,b,5,c,8,a,4,e,11'
x = x.replace(","," ")
x = x.split()
c = {}
for i in x:
    if i.isalpha():
        n = i
        c.setdefault(n)
    elif i.isdigit():
         b = i
         c[n]=b
print(c)
