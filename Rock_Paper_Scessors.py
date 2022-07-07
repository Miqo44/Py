"""Game Rock, Paper, Scissors"""
import random
x = input("Rock/Paper or Scessors>")
y = random.randint(0,2)
if y == 0:
    y = "Rock"
elif y == 1:
    y = "Paper"
else:
    y = "Scessors"
if x == y:
    print("Equal")
elif x == "Rock" and y == "Scessors":
    print ("You win")
elif x == "Paper" and y == "Rock":
    print ("You win")
elif x == "Scessors" and y == "Paper":
    print ("You win")
elif x == "Rock" and y == "Paper" or x == "Paper" and y == "Scessors":
    print ("You lose")
else:
    print ("You lose")
print(x+" Your chose,",y+" Computer chose")
