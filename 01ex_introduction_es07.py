# EXCERSICE 7

print ("-------------Excersice 7: Cubes-----------------")
print ("-------------FOR LOOP-----------------")

cubes = []

for i in range(0, 10):
    cubes.append(i**3)

print(cubes)

print ("-------------LIST COMPREHENION-----------------")

cubes1 = [x**3 for x in range(10)]
print(cubes1)