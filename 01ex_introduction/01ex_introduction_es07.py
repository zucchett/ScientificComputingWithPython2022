cubes = []
for i in range(11):
    cubes.append(i**3)

print('This list is produced by for loop:\n',cubes)

num = [x**3 for x in range(11)]
print("This list is produced by list comprehension:\n",num)


