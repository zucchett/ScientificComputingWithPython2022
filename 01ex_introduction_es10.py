#Please insert your vector on the line below:
vector_1 = float(input("insert the s:"))
vector_2= float(input("insert the h:"))
vector_3= float(input("insert the m:"))
vector=(vector_1,vector_2,vector_3)
mylist1 , sum = [] , 0
for i in vector:
    sum = sum + i**2
dist = sum**0.5
print(f"The normalized vector is: \n{[i/dist for i in vector]}")
