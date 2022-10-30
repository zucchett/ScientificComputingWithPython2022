cubesList = []
for i in range(0,11):
    y = i**3
    cubesList.append(y)
print("A: Cubes of items : ", cubesList)

secondList = [i**3 for i in range(0,11)]
print("B: Cubes of items in List Comprehension: ", secondList)