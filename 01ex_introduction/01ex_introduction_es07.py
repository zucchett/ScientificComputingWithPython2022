#7. Cubes

#a)A list of the cubes of x for x in [0, 10] with a for loop
l=[]
for i in range(11):
    l.append(i**3)
print("The list of the cubes of x for x in [0, 10] is:",l)

#b)A list of the cubes of x for x in [0, 10] with a list comprehension
l=[x**3 for x in range(11)]
print("The list of the cubes of x for x in [0, 10] is:",l)
