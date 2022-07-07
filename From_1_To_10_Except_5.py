"""Display the numbers from 1 to 10 except 5. Expected Output: 1 2 3 4 5 7 8 9 10"""
for i in range(1,11):
    if i == 5:
        continue
    print(i)
