# 8\. **List comprehension**
# Write, using the list comprehension, a single-line expression that gets the same result as the code in the cell below.
a = []
for i in range(3):
    for j in range(4):
        a.append((i, j))
print(a)

# List comprehension
newA = [(i, j) for i in range(3) for j in range(4)]
print(newA)

