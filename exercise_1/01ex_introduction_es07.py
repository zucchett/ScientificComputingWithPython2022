cubesList = []
for x in range(11):
    y = x**3
    cubesList.append(y)
print("A: Cubes of x using for loop: ", cubesList)

secondList = [x**3 for x in range(11)]
print("B: Cubes of x using List Comprehension: ", secondList)
