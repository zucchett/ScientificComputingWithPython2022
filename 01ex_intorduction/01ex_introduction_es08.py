# 8. List comprehension

# Write, using the list comprehension, a single-line expression that gets the same result as
# the code in the cell below.

print('# ----------- Method 1 -------------- #')


a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

print('# ----------- Method 2 -------------- #')

cubes = [x**2 for x in range(0,10)]
print(cubes)
