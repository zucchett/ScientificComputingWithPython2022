for_loop_cubes=[]
for i in range (0,11):
    for_loop_cubes.append(i**3)

list_comprehension_cubes=[pow(i,3) for i in range(0,11)]

print(for_loop_cubes)
print(list_comprehension_cubes)