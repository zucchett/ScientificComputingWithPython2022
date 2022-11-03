# Normalization of a N-dimensional vector

v1 = float(input("Insert the x:"))
v2 = float(input("Insert the y:"))
v3 = float(input("Insert the z:"))

vector = (v1, v2, v3)
list , sum = [] , 0
for i in vector:
    sum = sum + i**2
dist = sum**0.5
print(f"The normalized vector is: \n{[i/dist for i in vector]}")
