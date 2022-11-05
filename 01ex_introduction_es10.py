#Please insert your vector on the line below:
vec_1 = float(input("enter the x:"))
vec_2 = float(input("enter the y:"))
vec_3 = float(input("enter the z:"))
vector = (vec_1,vec_2,vec_3)

list1 , sum = [] , 0
for i in vector:
    sum = sum + i**2
dist = sum**0.5
print(f"The normalized vector is: \n{[i/dist for i in vector]}")
