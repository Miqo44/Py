"""Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
if employee is female, then she will work only in urban areas.
if employee is a male and age is in between 20 to 40 then he may work in anywhere
if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
And any other input of age should print "ERROR"."""
x = int(input("your age>"))
y = input("your gender M or F>")
z = input("your marital status Y or N>")
if y == "F":
    print ("you can work only urban areas")
elif y == "M" and x >= 20 and x < 40:
    print ("you can work anywhere")
elif y == "M" and x >= 40 and x < 60:
    print ("you can work only urman areas")
else:
    print ("ERROR")
