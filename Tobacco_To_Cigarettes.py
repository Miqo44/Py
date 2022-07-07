'''Write a python program where you have one input the grams of tobacco and you know that 20 grams tobacco is one cigarettes .
for example 
sample input: 327 grams
output: 16 cigarettes'''
x = int(input("Enter grams of tobacco > "))
y = x //20
print (str(x) + " grams of tobacco is " + str(y) + " Cigarettes!")
