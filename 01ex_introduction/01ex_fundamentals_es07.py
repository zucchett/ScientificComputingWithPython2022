# 7. Cubes

# Create a list of the cubes of x for x in [0, 10] using:

# a) a for loop

# b) a list comprehension

cubes_loop = []

for i in range(11) :
    cubes_loop.append(i**3)

print("The list of the cubes from 0 to 10 created with a loop is " + str(cubes_loop))

cubes_compr = [i**3 for i in range(11)]

print("The list of the cubes from 0 to 10 created with a list comprehension is " + str(cubes_compr))