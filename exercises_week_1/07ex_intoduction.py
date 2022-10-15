#7. Cubes

#output
for_cubes = []
compre_cubes =[]

#a. for loop
for i in range(0,10):
    for_cubes.append(i**3)

print(f"This is the result with the FOR LOOP: {for_cubes}")

#b. list comprehension
compre_cubes = [x**3 for x in range(0,10)]
print(f"This is the result with the FOR LOOP: {compre_cubes}")