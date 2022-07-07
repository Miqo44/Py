"""The given character is an uppercase letter or lowercase letter or a digit or a special character.
input      >>  @
output   >>   @ - Special character"""

x = input()
if x.isupper():
    print (x +"-Uppercase")
elif x.islower():
    print (x +"-Lowercase")
elif x.isdigit():
    print (x +"-Digit")
else:
    print (x +"Special character")
