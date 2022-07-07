"""You are given a program that takes all 3 passengers ages as inputs and inserts them in a list.
Complete the program so that if it finds a value less than 16,
it breaks the loop and outputs "Too young! ".
If the age requirement is satisfied, the program outputs "Get ready!"."""
x = {'arman': 27,'greta': 15,'armen':37}
y = []
def tariq():
    for i in x.values():
        if i < 16:
            global y
            y = "Too young"
            break
        else:
            n = "Get ready"
    if y == "Too young":
        print(y)
    else:
        print(n)
tariq()
