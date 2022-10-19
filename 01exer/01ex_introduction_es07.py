#Alexandru Timis, 2039336, alexandru.timis@studenti.unipd.it
#for loop method
i = 0
cube = []
for i in range(11):
    x = i**3
    i += i
    cube.append(x)

#print(cube)

#####################################################################################################
# list comprehension method

cubes = [x**3 for x in range(11)]
#print(cubes)

if cube == cubes:
    print("The two methods are equivalent")
else:
    print("The program DOES NOT WORK")