"""Write a Python program to find name in tuple."""
x = ('Anna','Alina','Amir','Susik')
y = input("Enter name > ")
for i in x:
    if y in x:
        print (str(y)+" < anun@ arka e!")
        break
    else:
        print("Anun@ arka che.")
        break
