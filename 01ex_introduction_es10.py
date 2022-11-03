#Please insert your vector on the line below:
vector = (1,0,0,5,8,9,20)

list1 , sum = [] , 0
for i in vector:
    sum = sum + i**2
dist = sum**0.5
print(f"\nThe normalized vector is: \n{[i/dist for i in vector]}\n")
