# Cubes

list_of_cube_1 = []
list_of_cube_2 = []

for i in range(11):
    list_of_cube_1.append(pow(i,3))
print(list_of_cube_1)

list_of_cube_2 = [pow(x,3) for x in range(11)]
print(list_of_cube_2)