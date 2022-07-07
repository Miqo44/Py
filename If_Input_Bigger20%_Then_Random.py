"""You (input) and pc have followers (pc have random followers) if your followers
is great 20 % than pc you are blogger otherwise pc is blogger."""
import random
x = random.randint(0,100)
y = int(input("hetevortneri qnak>"))
if (y/100)*20 > x:
    print ("You are blogger")
else:
    print ("PC are blogger")
