# 8. List comprehension

# Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.

b = []

b = [(i, j) for i in range(3) for j in range(4)]
print(b)