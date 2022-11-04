x = []

#for loop
for i in range(10):
    x.append(i**3)
    
print("List of cubes using for loop \n",x)

#list comprehension
y = [j**3 for j in range(10)]
print("List of cubes using list comprehensionp \n",y)

