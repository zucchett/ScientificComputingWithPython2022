# 7. Cubes

# Create a list of the cubes of x for x in [0, 10] using:

# a) a for loop

print('# ----------- Question a -------------- #')
cubes = []
for x in range(0,11):
    cubes.append(x**3)
print(cubes)

# b) a list comprehension

print('# ----------- Question b -------------- #')
cubes = [x**3 for x in range(0,11)]
print(cubes)
