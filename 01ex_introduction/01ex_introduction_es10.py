vector=(4.7, 8, 7.3)
mylist1 , sum = [] , 0
for i in vector:
    sum = sum + i**2
dist = sum**0.5
print(f"The normalized vector is: \n{[i/dist for i in vector]}")
