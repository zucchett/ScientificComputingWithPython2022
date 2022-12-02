#ex_07

#Create a list of the cubes of x for x in [0, 10] using:

#a) a for loop

cubes = []

for x in range (0, 10):
    cubes.append(x*x*x)

print (cubes)


#b) a list comprehension

cubes1 = [x*x*x for x in range (0,10)]
print (cubes1)
